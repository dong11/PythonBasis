from xml.parsers.expat import ParserCreate
import re


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

print('**************解析一段天气信息的XML*********************')

data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''


# class WeatherSaxHandler(object):
#     def init(self):
#         self.weather = {'today': {}, 'tomorrow': {}}
#
#     def start_e(self, name, attrs):
#         self.name = name
#         self.attrs = attrs
#
#     def end_e(self, name):
#         if name == 'pubDate':
#             self.today = int(re.search(r'\d+', self.content).group(0))
#         elif name == 'yweather:forecast':
#             day = int(re.search(r'\d+', self.attrs['date']).group(0))
#             if day - self.today == 0:
#                 self.weather['today']['date'] = day
#                 self.weather['today']['low'] = self.attrs['low']
#                 self.weather['today']['high'] = self.attrs['high']
#                 self.weather['today']['text'] = self.attrs['text']
#             elif day - self.today == 1:
#                 self.weather['tomorrow']['date'] = day
#                 self.weather['tomorrow']['low'] = self.attrs['low']
#                 self.weather['tomorrow']['high'] = self.attrs['high']
#                 self.weather['tomorrow']['text'] = self.attrs['text']
#             pass
#
#     def c_data(self, content):
#         self.content = content

def setDayInfo(dayInfo, content):
    dayInfo['low'] = int(content['low'])
    dayInfo['high'] = int(content['high'])
    dayInfo['text'] = content['text']


class WeatherSaxHandler(object):
    def init(self):
        self.weather = {'today': {}, 'tomorrow': {}}

    def start_e(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def end_e(self, name):
        if name == 'pubDate':
            self.today = int(re.search(r'\d+', self.content).group(0))
        elif name == 'yweather:location':
            self.weather['city'] = self.attrs['city']
            self.weather['country'] = self.attrs['country']
        elif name == 'yweather:forecast':
            day = int(re.search(r'\d+', self.attrs['date']).group(0))
            if day - self.today == 0:
                setDayInfo(self.weather['today'], self.attrs)
            elif day - self.today == 1:
                setDayInfo(self.weather['tomorrow'], self.attrs)

    def c_data(self, content):
        self.content = content


def parse_weather(data):
    parser = ParserCreate()
    handler = WeatherSaxHandler()
    parser.StartElementHandler = handler.start_e
    parser.EndElementHandler = handler.end_e
    parser.CharacterDataHandler = handler.c_data
    handler.init()
    parser.Parse(data)
    return handler.weather

print(parse_weather(data))
