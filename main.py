import requests
import datetime


def time_convert(date):
    return round(datetime.datetime.strptime(date, "%d/%m/%Y").timestamp())


class SOFParser:

    def __init__(self, tag, from_date, to_date):
        self.tag = tag
        self.from_date = from_date
        self.to_date = to_date

    def params(self, page_number):
        from_date_conv = time_convert(self.from_date)
        to_date_conv = time_convert(self.to_date)
        return {
            'fromdate': f'{from_date_conv}',
            'todate': f'{to_date_conv}',
            'tagged': 'python',
            'site': 'stackoverflow',
            'page': page_number,
            'pagesize': '100',
        }

    def get_all_data(self, page=1, question_count=0):
        params = self.params(page)
        response = requests.get('https://api.stackexchange.com/2.3/questions', params=params)
        json_data = response.json()
        print(f'PAGE NUMBER {page}')
        for title in json_data['items']:
            question_count += 1
            print(question_count, title['title'])
        while json_data['has_more']:
            page += 1
            return self.get_all_data(page, question_count)


if __name__ == '__main__':
    from_date = '8/02/2022'
    to_date = '10/02/2022'
    SOFParser('python', from_date, to_date).get_all_data()
