# Testops Robot
TestOps Robot for Python language.

## Usage

### Configuration

#### Environment variables

Configurations will be read from environment variables, and properties file in this order.

* `TESTOPS_SERVER_URL`

    Katalon TestOps endpoint (default: `https://testops.katalon.io`).

* `TESTOPS_API_KEY`

    Your Katalon TestOps API Key.

* `TESTOPS_PROJECT_ID`

    The Katalon TestOps project that will receive the test results.

* `TESTOPS_BASELINE_COLLECTION_ID`

    The Baseline Collection will choose to compare with checkpoints created by the test and support continuous testing with AI - Visual Testing.

* `TESTOPS_REPORT_FOLDER`

    The local directory where test results will be written to (default: `testops-report`).

* `TESTOPS_PROXY_SERVER_TYPE`

* `TESTOPS_PROXY_HOST`

* `TESTOPS_PROXY_PORT`

* `TESTOPS_PROXY_USERNAME`

* `TESTOPS_PROXY_PASSWORD`


#### Configuration file

Create a `testops-config.json` file in the top-level directory.

```
{
    // Default value: https://testops.katalon.io
    "basePath": "",
    "apiKey": "",
    "projectId": "",
    // Support continuous testing with AI - Visual Testing
    "baselineCollectionId": "",
    // Default value: testops-report
    "reportFolder": "",
    "proxy": {
        "protocol": "", // Value: http, https
        "host": "",
        "port": "",
        "auth": {
            "username": "",
            "password": ""
        }
    }
}

```

#### Install testops-robot plugin
```
pip3 install testops-robot
```
#### Run with robot with listener
```
robot --listener testops.Listener <file .robot>
```
## Samples
```
TODO: create sample repo for robot framwork in katalon
```