import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

rss_elemaent = xml_tree.Element('rss', {'version':'2.0','xmlns:p':'http://world.episerver.com/feeds/EpiserverRSS20.xsd'})
channel_element = xml_tree.SubElement(rss_elemaent, 'channel')

link_prefix = yaml_data['link']

xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'format').text = yaml_data['format']
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']
xml_tree.SubElement(channel_element, 'p:image', {'href': link_prefix + yaml_data['image']})
xml_tree.SubElement(channel_element, 'language').text = yaml_data['language']
xml_tree.SubElement(channel_element, 'link').text = link_prefix

xml_tree.SubElement(channel_element, 'p:category', {'text': yaml_data['category']})

for item in yaml_data['item']:
    item_element = xml_tree.SubElement(channel_element, 'item')
    xml_tree.SubElement(item_element, 'title').text = item['title']
    xml_tree.SubElement(item_element, 'itunes:author').text = yaml_data['author']
    xml_tree.SubElement(item_element, 'description').text = item['description']
    xml_tree.SubElement(item_element, 'itunes:duration').text = item['duration']
    xml_tree.SubElement(item_element, 'pubData').text = item['published']


    eclosure = xml_tree.SubElement(item_element, 'enclosure', {
        'url': link_prefix + item['file'], 
        'type': 'audio/mpeg', 
        'lenght': item['length']
        })


output_tree = xml_tree.ElementTree(rss_elemaent)
output_tree.write('podcast.xml', encoding='utf-8', xml_declaration=True)