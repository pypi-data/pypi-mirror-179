# Pulsar Producer

CLI that allows to send a message into a Apache Pulsar topic

#

Usually, implementing an Apache Pulsar Consumers, you will need to test it before release. Then, it's quite painful that you need to write or change some code in order to test it. Having that said, I have implemented this CLI that can help you with that.

Now, you can have a file with the message you want to send into a specific Apache Pulsar Topic and simply test your Apache Pulsar Consumer easily.

# How to use it

First, you should install the CLI on your machine

`pip install pulsar-producer` or `pip install --user pulsar-producer` if you want make it available only for your user.

> **_NOTE:_**  This package still *not* publish on pypi, only on [testing environment](https://test.pypi.org/project/pulsar-producer/0.1.0/#description)

> **_NOTE:_** pip install -i https://test.pypi.org/simple/ pulsar-producer==0.1.0

Then, you need to have an file with your Apache Pulsar server address. This file SHOULD follow a JSON format.

Example:

[_my-apache-pulsar-configuration.json_](./examples/pulsar-connection.json)

```json
{
        "host": "localhost",
        "port": "6650",
        "topic": "my-topic-name"
}

```

Then, you need to have another file with contains the message you want to publish in your Apache Pulsar topic in order to test your Apache Pulsar Consumer.
This file can contains ANYTHING you want. In this example, let's say you want to publish a JSON structure message.

[_my-message-file-example.json_](./examples/message-file)

```json
{
    "KEY": "THIS IS MY MESSAGE WHICH COULD BE ONLY PURE TEXT (NOT JSON)"
}

```

Now, you just need to run:

`pulsar-producer --pulsar-connection-file ./path-of-your-my-apache-pulsar-configuration-example-json --message-file ./path-or-your-message-file`

# License
MIT
