from pytest import mark
from automation_tools.selenium.pages.languages_page import LanguagesPage
from selenium.common.exceptions import TimeoutException
from re import sub
from dataclasses import dataclass, asdict


@dataclass(frozen=True, order=True)
class LanguagesTable:
    """
    Use this to save table rows as dataclass objects
    """
    website: str
    visitors: int
    frontend: list
    backend: list
    db: list
    notes: str


def remove_footnotes(data_to_clean: str) -> str:
    """This function removes footnotes from data

    example: 'Bigtable,[4] MariaDB[5]' -> 'Bigtable, MariaDB'
    """
    return sub(r'\[.*?\]', '', data_to_clean)


def clean_data(data_to_clean: str) -> list:
    """This function converts
    'comma-separated lists' into actual lists,
    it also removes empty strings and
    strips words of empty spaces

    example: 'Bigtable, MariaDB ' -> ['Bigtable', 'MariaDB']
    """
    list_of_stripped_strings = remove_footnotes(data_to_clean).split(',')
    tidy_data = [item.strip() for item in list_of_stripped_strings if item != '']
    return tidy_data


def scrap_data_from_wiki_table(driver) -> list:
    """This function scraps data from the wiki page
    and presents it in a list of dicts* format
    where each dict is a row with tidy data

    *dicts are converted dataclass objects"""

    # get POM objects for the wiki page
    languages_page = LanguagesPage(driver)

    # go to the page
    site_url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'
    languages_page.go(site_url)

    # this will be populated with a dict object with clean data from the table
    rows = []

    last_index = False
    index = 0
    while not last_index:
        try:
            index += 1

            # extract data
            website = languages_page.cell_contents_by_row_cell(index, 1).text
            num_of_visitors = languages_page.cell_contents_by_row_cell(index, 2).text
            frontend = languages_page.cell_contents_by_row_cell(index, 3).text
            backend = languages_page.cell_contents_by_row_cell(index, 4).text
            db = languages_page.cell_contents_by_row_cell(index, 5).text
            notes = languages_page.cell_contents_by_row_cell(index, 6).text

            # clean data
            num_of_visitors = int(
                remove_footnotes(num_of_visitors).split(' ')[0].strip().replace('.', '').replace(',', ''))
            website = remove_footnotes(website).strip()
            frontend = clean_data(frontend)
            backend = clean_data(backend)
            db = clean_data(db)
            if notes == '': notes = None

            # dataclass dict object representing an entry for a site
            site = asdict(LanguagesTable(website, num_of_visitors, frontend, backend, db, notes))

            # append dataclass dicts to list of rows
            rows.append(site)

        # this exception is triggered when index is out of range
        except TimeoutException:
            last_index = True

    return rows


@mark.parametrize("monthly_users", [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 1.5 * 10**9])
def test_languages_page(driver, log, monthly_users):
    """This test checks each row of the wiki table
    to find if an entry has less monthly users that expected.

    If an entry has fewer users than expected it raises an exception.
    """
    # instantiate logs
    log.create(f'popular_languages_{monthly_users}')

    log.add_step(f'see if any site has fewer than {int(monthly_users)} visitors\n')

    # get list of dicts where each dict is a row with clean data
    rows = scrap_data_from_wiki_table(driver)

    # iterate through each row, append rows that don't qualify
    # to a new list
    rows_with_too_few_monthly_visitors = []
    for row in rows:
        if row['visitors'] < monthly_users:
            rows_with_too_few_monthly_visitors.append(row)

    log.add_step('FULL TABLE')
    for row in rows:
        log.add_step(str(row))

    # if there are sites with too few visitors raise an exception
    if len(rows_with_too_few_monthly_visitors) > 0:
        exception_message = ''

        log.add_step('\nSITES THAT HAD TOO FEW VISITORS')

        # format data to be presented by the exception
        for row in rows_with_too_few_monthly_visitors:

            log.add_step(str(row))

            frontend = ', '.join(row['frontend'])
            backend = ', '.join(row['backend'])

            difference = int(monthly_users) - row['visitors']

            message = f"""
            {row['website']} (Frontend:{frontend}\Backend:{backend}) 
            has {row['visitors']} unique visitors per month. 
            (Expected more than {int(monthly_users)})\n
            The site must add {difference} additional visitors to pass the test.
            """
            if exception_message == '':
                exception_message = message
            else:
                exception_message = exception_message + "\n" + message

        # raise the exception listing all rows that have not qualified
        raise Exception(exception_message)
