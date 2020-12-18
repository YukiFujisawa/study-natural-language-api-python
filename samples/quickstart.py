#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def run_quickstart():
    # [START language_quickstart]
    # Imports the Google Cloud client library
    # [START language_python_migration_imports]
    from google.cloud import language_v1

    # [END language_python_migration_imports]

    # Instantiates a client
    # [START language_python_migration_client]
    client = language_v1.LanguageServiceClient()
    # [END language_python_migration_client]

    # Detects the sentiment of the text
    text = input().strip()
    # text = u"全体としては面白かったです。ただ、あんなに強かったラスボスを倒す流れが謎すぎました。個人的に映画はラスト重視なので、この終わり方はちょっとなぁ。"
    document = language_v1.types.Document(
        content=text,
        type='PLAIN_TEXT',
    )
    response = client.analyze_sentiment(
        document=document,
        encoding_type='UTF8',
    )
    sentiment = response.document_sentiment

    print(response.sentences)

    print("Text: {}".format(text))
    print("Sentiment: \n sentiment.score:{}, \n sentiment.magnitude:{}".format(sentiment.score, sentiment.magnitude))
    # [END language_quickstart]


if __name__ == "__main__":
    run_quickstart()
