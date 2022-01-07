# https://gist.github.com/rotemtam/88d9a4efae243fc77ed4a0f9917c8f6c

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
from pathlib import Path

def pascaltocsv(path):
    xmllist = []

    for xmlfile in glob.glob(path + '/*.xml'):
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        for member in root.findall('object'):
            bbx = member.find('bndbox')
            xmin = int(bbx.find('xmin').text)
            ymin = int(bbx.find('ymin').text)
            xmax = int(bbx.find('xmax').text)
            ymax = int(bbx.find('ymax').text)
            label = member.find('name').text

            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     label,
                     xmin,
                     ymin,
                     xmax,
                     ymax
                     )
            
            xmllist.append(value)
    column_name = ['filename', 'width', 'height',
                   'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xmllist, columns=column_name)
    return xml_df


def main():
    datasets = ['train', 'dev', 'test']

    path = 'D:/Documents/TSU_ProjectF21/imagelabelling/labelImg/images/paperballs'
    xml_df = pascaltocsv(path)
    xml_df.to_csv('labels_{}.csv'.format('dataset'), index=None)
    print('Successfully converted xml to csv.')


main()