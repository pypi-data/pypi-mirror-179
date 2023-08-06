# Falcon Sandbox python library

Python library for the [Falcon Sandbox API](https://www.falcon-sandbox.com/docs/api/v2) with command line wrapper. Library originally developed for use by [ACE](https://github.com/ace-ecosystem/ACE). The command line wrapper was written to more easily interact with a Falcon Sandbox for intel analysts and [Event Sentry](https://github.com/ace-ecosystem/eventsentry) consumption.

## Installation

``pip install falcon-sandbox``

## The falcon-sandbox CLI script

When installed, a command line script named 'falcon-sandbox' is supplied that can be used to interact with a Falcon Sandbox service.

The command line script looks for the configuration settings it needs at ``~/<current-user>/.config/falcon.ini``. The script will prompt you for the information it needs and write that file on the first execution if the file doesn't already exist. Like so:

```
$ falcon-sandbox
2022-12-01 21:47:04 ace-dev2 falcon_sandbox.helpers.load_config[1112363] CRITICAL Didn't find any config files defined at these paths: ['/data/home/user/.config/falcon.ini']
Did not find user configuration, would you like to create one? [Y/n]Y
Client ID of your API client: 2d21b31ed3543rffe333ce872bf5111
Client secret associated with the client ID: 3OxAA30EexkYi17BoOOhJwDHFxpusA23zd23a4axz
Do you need to use the system proxy to connect to the sandbox? [Y/n] N
2022-12-01 21:48:59 ace-dev2 root[1112363] INFO Wrote user configuration to: /data/home/user/.config/falcon.ini
```

The root level help:
```
$ falcon-sandbox -h
usage: falcon-sandbox [-h] [-d] [--ignore-proxy] [--client-id CLIENT_ID] [--client-secret CLIENT_SECRET] {submit,query,get,delete} ...

A command line client for interacting with the Falcon Sandbox library written for the ACE Ecosystem.

positional arguments:
  {submit,query,get,delete}
    submit              Upload and submit a sample
    query               Query existing hashes, reports in our sandbox
    get                 Get samples, artifacts, and results from the server
    delete              Delete reports or samples

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Set logging to DEBUG
  --ignore-proxy        Ignore system proxy
  --client-id CLIENT_ID
                        Pass client id to use. Overrides config
  --client-secret CLIENT_SECRET
                        Pass client secret to use. Overrides any configured client secrect
```

## Examples

### Submit

Submit files and URLS. The default behavior for the command line is to wait for the completion of jobs that are submitted and then download the entire result as json.

#### Files

For submissions from the command line the default behavior is to wait for the submission to complete and download all results as json.
Be aware the result files can be quite large. They are chunked on download for that reason.
```
$ falcon-sandbox submit -f PMNT_089_08102019.xls -e 100
2022-12-01 22:13:49 ace-dev2 falcon_sandbox[1114996] INFO Uploading file...
2022-12-01 22:13:50 ace-dev2 falcon_sandbox[1114996] INFO File uploaded sucessfully. Got the file's SHA256 and its name
[{'sha256': '640deec892a7f8110eb0348f2546a8811ff9ed217ccdb7d6b65c46b20fe95964', 'file_name': 'WEEK  13  2022 xls'}]
2022-12-01 22:13:50 ace-dev2 falcon_sandbox[1114996] INFO Got submission id 25ebccb63ffb4061889c708a87b55a2d_21edf1887ebd45adb8cf800d5ab3f5bb for your submission
2022-12-01 22:13:52 ace-dev2 falcon_sandbox[1114996] INFO Submission 25ebccb63ffb4061889c708a87b55a2d_21edf1887ebd45adb8cf800d5ab3f5bb is in RUNNING state...
2022-12-01 22:14:01 ace-dev2 falcon_sandbox[1114996] INFO Submission 25ebccb63ffb4061889c708a87b55a2d_21edf1887ebd45adb8cf800d5ab3f5bb is in RUNNING state...
...
2022-12-01 22:21:13 ace-dev2 falcon_sandbox[1114996] INFO Submission 25ebccb63ffb4061889c708a87b55a2d_21edf1887ebd45adb8cf800d5ab3f5bb is in RUNNING state...
2022-12-01 22:21:13 ace-dev2 falcon_sandbox[1114996] INFO Submission 25ebccb63ffb4061889c708a87b55a2d_21edf1887ebd45adb8cf800d5ab3f5bb has moved to SUCCESS state
2022-12-01 22:21:13 ace-dev2 falcon_sandbox[1114996] INFO Wrote 25ebccb63ffb4061889c708a87b55a2d_21edf1887ebd45adb8cf800d5ab3f5bb.falcon.json
```

#### URLs

```
$ falcon-sandbox submit -u 'https://firebasestorage.googleapis.com/v0/b/gu0-81b2b.appspot.m/o/index.html'
2022-12-02 02:15:54 ace-dev2 falcon_sandbox[1122593] INFO Got submission id 25ebccb63ffb4061889c708a87b55a2d_cc5a4e7eed724adabd9d2fcdf602fe97 for your submission
2022-12-02 02:15:56 ace-dev2 falcon_sandbox[1122593] INFO Submission 25ebccb63ffb4061889c708a87b55a2d_cc5a4e7eed724adabd9d2fcdf602fe97 is in RUNNING state...
2022-12-02 02:16:05 ace-dev2 falcon_sandbox[1122593] INFO Submission 25ebccb63ffb4061889c708a87b55a2d_cc5a4e7eed724adabd9d2fcdf602fe97 is in RUNNING state...
...
2022-12-02 02:34:41 ace-dev2 falcon_sandbox[1122593] INFO Submission 25ebccb63ffb4061889c708a87b55a2d_cc5a4e7eed724adabd9d2fcdf602fe97 is in RUNNING state...
2022-12-02 02:34:41 ace-dev2 falcon_sandbox[1122593] INFO Submission 25ebccb63ffb4061889c708a87b55a2d_cc5a4e7eed724adabd9d2fcdf602fe97 has moved to SUCCESS state
2022-12-02 02:34:41 ace-dev2 falcon_sandbox[1122593] INFO Wrote 25ebccb63ffb4061889c708a87b55a2d_cc5a4e7eed724adabd9d2fcdf602fe97.falcon.json
```

### Get

Get samples, analysis summaries, and all the various report data.

#### Get report summary

```
$ falcon-sandbox get report -sum 25ebccb63ffb4061889c708a87b55a2d_f375984f7ac54d309cfb056bea724b4f | grep "sandbox" -A 15
  "sandbox": [
      {
          "sha256": "2c1d108fbb59bc295e862833324598367ed7f72ea2d38c115af2ec57332447e0",
          "environment_id": 110,
          "environment_description": "Windows 7 64 bit",
          "submit_name": "Plan_Appro_22075_2022.12.01.xls",
          "submission_type": "file",
          "verdict": "no specific threat",
          "file_type": "Composite Document File V2 Document, Little Endian, Os: Windows, Version 10.0, Code page: 1252, Author: floresq, Last Saved By: hollardt, Name of Creating Application: Microsoft Excel, Last Printed: Thu Dec  1 13:00:32 2022, Create Time/Date: Thu Dec  1 10:51:04 2022, Last Saved Time/Date: Thu Dec  1 13:00:53 2022, Security: 0",
          "sample_flags": [
              "Extracted Files"
          ],
          "network_settings": "default"
      }
  ],
  "verdict": "no specific threat",
```

#### Get/Download the original sample using sha256 hash

```
$ falcon-sandbox get sample 640deec892a7f8110eb0348f2546a8811ff9ed217ccdb7d6b65c46b20fe95964
2022-12-02 02:41:10 ace-dev2 falcon_sandbox[1125306] INFO Found sample. Attempting to write it...
2022-12-02 02:41:10 ace-dev2 falcon_sandbox[1125306] INFO Wrote 640deec892a7f8110eb0348f2546a8811ff9ed217ccdb7d6b65c46b20fe95964
```

#### Get the entire report as json

```
$ falcon-sandbox get report 25ebccb63ffb4061889c708a87b55a2d_21edf1887ebd45adb8cf800d5ab3f5bb -d
2022-12-02 02:41:48 ace-dev2 falcon_sandbox[1125365] INFO Wrote 25ebccb63ffb4061889c708a87b55a2d_21edf1887ebd45adb8cf800d5ab3f5bb.falcon.json
$
$ cat 25ebccb63ffb4061889c708a87b55a2d_21edf1887ebd45adb8cf800d5ab3f5bb.falcon.json | jq '.' | grep verdict -B 5 -A 5
  "cid": "25ebccb63ffb4061889c708a87b55a2d",
  "created_timestamp": "2022-12-01T22:13:50Z",
  "origin": "apigateway",
  "verdict": "suspicious",
  "ioc_report_strict_csv_artifact_id": "2d68eaaf3fb164b1ea0826c5ede3d8a773b430a9ed3606bd94d60ada914ba958",
  "ioc_report_broad_csv_artifact_id": "2d68eaaf3fb164b1ea0826c5ede3d8a773b430a9ed3606bd94d60ada914ba958",
  "ioc_report_strict_json_artifact_id": "0deea78a387e35480dc580d8871dfd6aba458e711e0ca594330a6162e5633583",
--
      ],
      "submit_name": "Week 13 2022.xls",
      "submission_type": "file",
      "verdict": "suspicious",
      "threat_score": 35,
      "windows_version_name": "Windows 7",
      "windows_version_edition": "Professional",
--
  ],
  "malquery": [
    {
      "verdict": "unknown",
      "input": "640deec892a7f8110eb0348f2546a8811ff9ed217ccdb7d6b65c46b20fe95964",
      "type": "sha256"
    }
```

### Query

Query by hash(es), submission_id(s)

#### Hashes

```
$ falcon-sandbox query hashes 2c1d108fbb59bc295e862833324598367ed7f72ea2d38c115af2ec57332447e0 01d8f83e0842e0aebab58ee088a3dcb9cac3f5598538a372b2bd447dcda0dd9a -id
[
    "25ebccb63ffb4061889c708a87b55a2d_f375984f7ac54d309cfb056bea724b4f",
    "25ebccb63ffb4061889c708a87b55a2d_7c8e103d63c84acaadfd215d114dece9"
]
```

#### Reports

```
$ falcon-sandbox query reports "created_timestamp:>'2022-11-29' + verdict:'malicious'"
[
    "25ebccb63ffb4061889c708a87b55a2d_6b08a1146aec414ba302cffc860ec93b",
    "25ebccb63ffb4061889c708a87b55a2d_12ae6fc71d9c43eab2295d3f6e283a7f",
    "25ebccb63ffb4061889c708a87b55a2d_77fc2972e5544ca4bf773ac9628f6f8c",
    "25ebccb63ffb4061889c708a87b55a2d_4084f337409a4194bfb5d6078eb05aea",
    "25ebccb63ffb4061889c708a87b55a2d_cbab22b35db54b9eb075a583e92d7d1b",
    "25ebccb63ffb4061889c708a87b55a2d_9deb3433f1434f038f44a98962dd7100"
]
```

#### Job States

 ```
 $ falcon-sandbox get report -st 25ebccb63ffb4061889c708a87b55a2d_f375984f7ac54d309cfb056bea724b4f 25ebccb63ffb4061889c708a87b55a2d_7c8e103d63c84acaadfd215d114dece9 | grep "state" -A 7
  "state": "success",
  "created_timestamp": "2022-12-01T13:29:06Z",
  "sandbox": [
      {
          "sha256": "2c1d108fbb59bc295e862833324598367ed7f72ea2d38c115af2ec57332447e0",
          "environment_id": 110,
          "submit_name": "Plan_Appro_22075_2022.12.01.xls"
      }
--
  "state": "success",
  "created_timestamp": "2022-12-01T18:20:22Z",
  "sandbox": [q
      {
          "sha256": "01d8f83e0842e0aebab58ee088a3dcb9cac3f5598538a372b2bd447dcda0dd9a",
          "environment_id": 110,
          "submit_name": "General_Terms_and_Conditions.pdf.pdf"
      }
```
