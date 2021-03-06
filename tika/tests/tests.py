#!/usr/bin/env python2.7
# encoding: utf-8
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
#python -m unittest tests.tests

import unittest
import tika.parser


class CreateTest(unittest.TestCase):
    "test for file types"

    def test_remote_pdf(self):
        'parse remote PDF'
        self.assertTrue(tika.parser.from_file(\
            'http://appsrv.achd.net/reports/rwservlet?food_rep_insp&P_ENCOUNTER=201504160015'))
    def test_remote_html(self):
        'parse remote HTML' 
        self.assertTrue(tika.parser.from_file(\
            'http://philadelphia.pa.gegov.com/_templates/551/RetailFood/_report_full.cfm?inspectionID=8B2C8CA4-8039-EC2C-F94DBD247613E5CC&domainID=551&userID=0'))
    def test_remote_mp3(self):
        'parese remote mp3'
        self.assertTrue(tika.parser.from_file(\
            'http://downloads.bbc.co.uk/podcasts/worldservice/6min_vocab/6min_vocab_20150511-1134a.mp3'))
    def test_remote_jpg(self):
        'parse remote jpg'
        self.assertTrue(tika.parser.from_file('http://www.defense.gov/multimedia/web_graphics/coastgrd/USCGb.jpg'))


if __name__ == '__main__':
	unittest.main()