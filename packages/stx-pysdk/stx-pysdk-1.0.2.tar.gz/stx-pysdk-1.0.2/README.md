# Welcome to SportsX SDK Documentation

# Overview

The STX SDK is a wrapper around the Sportsx Graphql APIs and Phoenix channels.
The SDK provides object-oriented APIs to connect with the available Sportsx APIs and socket channels.
The SDK is built on the following libraries:
 - GQL: https://github.com/graphql-python/gql
 - Websockets: https://github.com/aaugustin/websockets

## Compatibility

This library is compatible with the following versions of Python:

 - 3.7
 - 3.8
 - 3.9

## Setup

Install the requirements:

    pip install -r requirements.txt

## Project Structure
    - stxsdk
        - config
            - channels
            - configs
            - schema.graphql
        - services
            - authentication
            - base
            - channel
            - proxy
            - schema
            - selection
        - storage
            - singleton
            - user_storage
        - enums
        - exceptions
        - typings
        - utils

The SDK is composed of two key sections:

 - **Proxy** (the classes providing the low-level functionality)
 - **Client** (the services to be used for connectivity with the STX APIs).

All you need to use is **Client** services for the integration with the APIs.

There are two services available **StxClient** and **StxChannelClient**

 - **StxClient** provides sync operations, while
 - **StxChannelClient** provides connectivity with websocket channels.
