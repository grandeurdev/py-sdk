# Grandeur [![Version](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://cloud.grandeur.tech)

Building a smart (IoT) product is an art. It is about unifying the physical world with the digital one. When you connect a hardware to the web, magic happens. But it involves development across an immense technology stack. You need to develop your hardware, your apps to monitor/control your hardware and a server backend to manage both. Then if you are (somehow) done with the development, there comes the hardest part; you will have to scale it all as your userbase gonna grow.

We can understand this because we have been there.

Introducing Grandeur; A backend as a service (BaaS) platform for IoT. We have designed this platform so that you do not have to worry about the backend of your next big thing and you could focus on what matters the most; your hardware and apps. It is designed specifically to accelerate your IoT product development and push your product to market in weeks rather than in months or years.

## Why Grandeur

Grandeur is designed keeping in mind all the challenges a hardware engineer can face in developing and commercializing a smart (IoT) product. And we made available out-of-the-box APIs to help you integrate your devices and apps.

For example, you can use the **Auth API** to create *register* and *login* flows and make sure each user has access to its own data and no one other than the device admin itself should be able to interact with its device. You can store a humongous amount of data in cloud database to analyze and extract intelligent information from it and display useful graphs. Use our **datastore API** for that. You can host your product's website and your web app on Grandeur as well. It's **as simple as running literally a single command**. Also, your hardware device can listen for events and updates from your app, your app can listen for events and updates from your hardware device, and they can communicate with each other in realtime (with a latency of ~200ms). **Devices API** and **Device SDK** come into play here. But in no way would you have to waste your time in mixing and matching the APIs, checking which one works for your use case, and go through a huge learning curve -- like you would do while working with AWS or Google Cloud Platform. All the Grandeur APIs are completely integrated and speed and security is built in. The SDKs are designed around the whole ideology of **seamless integration.** 

Grandeur is not a regular IoT cloud. It's a complete IoT product development and management platform, designed for production environments. Here's how:

* Grandeur is product-centered. It is much more than just a medium of communication between your app and your hardware device. Focusing on expediting IoT product development, it offers an ecosystem of the most necessary tools integrated to make the most head-cracking development problems seamless. What problems you may ask?
  * Huge development stack (Your IoT product which is generally hardware, your web app, your server API, and the communication between all of these).
  * Your database design and management.
  * Setting up and maintaining your servers handling your compute, storage, and networking.
  * Web development (backend of your server, frontend of your web apps).
  * Your IoT product development itself.
  * Scaling your system up to hundreds of thousands of devices as your business grows.

* No need to mix and match various services to come up with your own solution. Grandeur is a single spot solution for all of your needs, from **built-in authentication** of your users and devices to **an integrated database** to an **out-of-the-box file storage system** and a registry of data for all of your devices. And You can manage absolutely everything from a single dashboard.

* Simple pricing. Unlike Google and AWS, we do not have to deal with a different pricing model for each service and aggregate them together to compute the monthly bill making it almost impossible for the user to understand why he has to pay this much! Packaging all our services into one platform has let us develop a very simple and transparent pricing model. You can [start free](https://cloud.grandeur.tech/) for a certain quota and then pay as you go based on your resources consumption. Checkout [pricing](https://grandeur.tech/pricing/) for more details.

* We have a growing [community on Hackster](https://www.hackster.io/grandeur) which is equivalent to growing number of developers which are using Grandeur and improving the opensource SDKs resulting in increasing Grandeur support.

* It is terrifically simple to [get started](https://cloud.grandeur.tech/) with your IoT product development. Just create a project from the [cloud dashboard](https://cloud.grandeur.tech/dashboard), plug your project's API key into our SDKs and start developing.

Follow [our Hackster Hub](https://www.hackster.io/grandeur) for quick starts and advanced development projects.

[Here](https://github.com/grandeurtech/js-sdk#get-started) is how you can create a new project on Grandeur and start using the Javascript SDK to build your IoT apps.

From here onwards, we'll look at how you can use the Py SDK for all arduino-compatible modules to put your devices live and connected on Grandeur. Let's dive in!

# Py SDK

**Py SDK** is the official SDK for Linux-based Raspberry Pis and SoCs and it utilizes the *Grandeur* API to connect your device to **[Grandeur](https://cloud.grandeur.tech/)**.

Follow the [get started](https://github.com/grandeurtech/py-sdk#get-started) guidelines to quickly get into the context of integrating your devices to Grandeur or jump straight to an [Py example](https://github.com/grandeurtech/py-sdk#example) to make your hands dirty.

For a developer reference for the Py SDK, you can have a look at the [documentation](#documentation).

To get a deeper understanding of the core concepts Grandeur is built upon, dive into the [Grandeur Ecosystem](#grandeur-ecosystem) section.

* [Get Started](#get-started)
  * [Installation](#installation)
  * [Inclusion](#inclusion)
  * [Setting Up Connection Event Handler](#setting-up-connection-event-handler)
  * [Fetching Device Variables and Updating Them](#fetching-device-variables-and-updating-them)
  * [Handling Updates From Grandeur](#handling-updates-from-the-cloud)
* [Example](#example)
* [The Dexterity of Py SDK](#the-dexterity-of-py-sdk)
* [Grandeur Ecosystem](#grandeur-ecosystem)
  * [A Brief Case Study](#a-brief-case-study)
  * [Concepts](#concepts)
    * [Project](#project)
    * [SDK](#SDK)
    * [User and Administrator](#user-and-administrator)
    * [Device](#device)
    * [Device Registry](#device-registry)
    * [Models](#models)
    * [Authentication and Access](#authentication-and-access)
    * [Networking](#networking)
    * [Allowed Origins](#allowed-origins)
* [Documentation](#documentation)
    * [init](#grandeur-init)
  * [Project](#project)
    * [isConnected](#isconnected)
    * [onConnection](#onconnection)
    * [device](#device)
  * [Device](#device)
    * [get](#get)
    * [set](#set)
    * [on](#on)

## Get Started

### Installation

1. You can install **Py SDK** using python's **pip**.
```sh
pip install grandeur
```

2. You can also clone **Py SDK** from [here](https://pypi.org/project/grandeur).

### Inclusion

This is how you can import the Py SDK in your RPi device.

```py
import grandeur.device as grandeur

# **RESULT**
# Includes the SDK in your sketch as grandeur.
```

### Initialization

Initialization is as simple as calling `grandeur.init()` with your credentials project's API Key and device's Access Token. The SDK uses your API key to select your project and access token to authenticate that the requests are coming from a legit device. It then returns your **project** reference which exposes the underlying features. For example, you can get a reference to this project's datastore by calling `datastore()` method or you can select a particular device by passing its device ID to `device()` method and then you can go programming your device from there.

```py
import grandeur.device as grandeur

# Init the SDK and get reference to the project
project = grandeur.init(ApiKey, DeviceToken)

# **RESULT**
# Initializes the SDK's configurations and returns your project reference.
```

As soon as you call `grandeur.init()`, the SDK uses the configurations to start trying to connect with the your project on Grandeur.

### Setting Up Connection Event Handler

You can also listen on SDK's connection-related events. For example, to run some code when the device makes a successful connection to Grandeur or when the device's connection to Grandeur breaks, you can wrap that code in a function and pass it to `Project`'s `onConnection()` function.

Here's how you can handle the connection event:

```py
import grandeur.device as grandeur

# Init the SDK and get reference to the project
project = grandeur.init(ApiKey, DeviceToken)

# This method handles the events related to device's connection with Grandeur.
def onConnection(state):
    # Prints the current state
    print(state)

# Setting up listener for device's connection event
project.onConnection(onConnection)

# **RESULT**
# Prints CONNECTED when device gets connected to Grandeur.
# And prints DISCONNECTED when device's connection from
# Grandeur breaks.
```

### Fetching Device Variables and Updating Them

On Grandeur, we generally store the device data in a sanboxed contianer. You can get and set data using the following functions of the `Data` class:

* `device.data().get()`
* `device.data().set()`

They are all **Async functions** because they communicate with Grandeur through internet. Communication through internet takes some time and we cannot wait, for example, for device's data variables to arrive from Grandeur — meanwhile blocking the rest of the device program. So, what we do is, we schedule a function to be called when the data variables and resume with rest of the device program, forgetting that we ever called `get()`. When the data variables arrive, the SDK calls our scheduled function, giving us access to data variables inside that function.

Read more about **Async functions** and `Callback` [here](#the-dexterity-of-py-sdk).

Here's how we would get and set device's data:

```py
import grandeur.device as grandeur

# This method handles the events related to device's connection with Grandeur.
def onConnection(state):
    # Prints the current state
    print(state)

# This function prints the variables stored in device
def getCallback(code, res):
    print(res["data"])

# This function prints the updated values of the variables
def setCallback(code, res):
    print(res["update"])

# Init the SDK and get reference to the project
project = grandeur.init(ApiKey, DeviceToken)

# Setting up listener for device's connection event
project.onConnection(onConnection)

# Get a reference to our device
device = project.device(DeviceID)

# Getting device data
device.data().get("", getCallback)

# Setting device's data
data = {"voltage": 220, "current": 10}

device.data().set("", data, setCallback)

# **RESULT**
# Data is fetched first. When they arrive from Grandeur, their
# corresponding callbacks are called which print the variables stored in data objects.
# Then the data is updated with the new values. When their updates complete, their
# callbacks are called with the updated values of their variables and these updated values are
# printed on the screen.
```

### Handling Updates From Grandeur

You can set **update handlers** for updates to those variables. Let's do that now:

```py
import grandeur.device as grandeur

# This method handles the events related to device's connection with Grandeur.
def onConnection(state):
    # Prints the current state
    print(state)

# This function prints the updated values of the variables stored
def updateCallback(path, update):
    print(update)

# Init the SDK and get reference to the project
project = grandeur.init(ApiKey, DeviceToken)

# Setting up listener for device's connection event
project.onConnection(onConnection)

# Get a reference to our device
device = project.device(DeviceID)

# Setting update handler for device variables
device.data().on("", updateCallback)

# **RESULT**
# Whenever an update in the device's data occur, the updated values of the
# variables are printed.
```

## Example

Here we go through a general example of a Raspberry Pi to explain the **Py SDK** in action.

To begin working with the **Py SDK**, the very first step is to [create a new project](https://cloud.grandeur.tech/) and [register a new device](https://cloud.grandeur.tech/devices) through the [Cloud Dashboard](https://cloud.grandeur.tech/dashboard). Then create a new python environment to keep your workspace packages isolated from the rest of the packages.

### Create and set up your workspace environment

Run the following:

```sh
python -m venv env
```

This will create a new folder named **env** in your working directory its own packages and libraries. `cd` into your workspace environment, and activate it.

```sh
cd env
source bin/activate
```

Install the **Py SDK** by running the command:

```sh
python -m pip install grandeur
```

### Import Py SDK into your Python program

After installing the **Py SDK**, you can import it into your sketch like this:

```py
import grandeur.device as grandeur 
```

### Initialize the SDK's Configurations

**Py SDK** takes care of your device's connection with Grandeur. To use it into your python program, you need to initialize its configurations first. You can do that using the `init` global method. Initializing the SDK returns a project reference which exposes all the SDK's functions.

```py
import grandeur.device as grandeur 

project = grandeur.init(ApiKey, YourToken)
```

You can find the API Key on the [settings page](https://cloud.grandeur.tech/settings) of your project's dashboard. For the Access Token, you need to pair your device with a user account in your project first. A device can only connect to Grandeur if it's paired with a user. And only the paired user can access the device's data through its web app. For convenient testing, we have made device pairing function available on the [devices page](https://cloud.grandeur.tech/devices) too. You can find your device's ID and pair your device with a user account. If your project has no registered user yet, you can add one easily from the [accounts page](https://cloud.grandeur.tech/accounts).

### Initialize Your Device

Before doing anything, you need to initialize your device with data from Grandeur to keep your device running in undefined states when it first starts. You can get all the device variables by using `get()` methods of the device. Here's how you can get the device **state** from Grandeur and initialize RPi's pin — we'll use the gpiozero package to interact with RPi's GPIOs for that.

```py
import grandeur.device as grandeur
from gpiozero import LED

# Selecting GPIO 17 to update the state of
led = LED(17)

project = grandeur.init(ApiKey, YourToken)
device = project.device(DeviceID)

def initializeState(code, res):
  print(res["data"])
  led.value = res["data"]

device.data().get("state", initializeState)

```

### Set Update Handlers

Update handlers are the functions which are called when a device variable is updated on Grandeur. The update could be from a user or the device itself. Without the handlers, your device would not be notified when a user turns it off from the webapp.
Here's how you can set update handlers in your sketch for the device's state stored.

```py
import grandeur.device as grandeur
from gpiozero import LED

# Selecting GPIO 17 to update the state of
led = LED(17)

project = grandeur.init(ApiKey, YourToken)
device = project.device(DeviceID)

def initializeState(code, res):
  print(res["data"])
  led.value = res["data"]

def updateState(path, update):
  print(update)
  led.value = update

device.data().get("state", initializeState)
device.data().on("state", updateState)

```

### Update Device Variables

To see the live state of the device on the web app, you need to keep sending the updated state after every few seconds. We'll use the `set()` function to update the state value.

```py
import grandeur.device as grandeur
from gpiozero import LED

# Selecting GPIO 17 to update the state of
led = LED(17)

project = grandeur.init(ApiKey, YourToken)
device = project.device(DeviceID)

def initializeState(code, res):
  print(res["data"])
  led.value = res["data"]

def updateState(path, update):
  print(update)
  led.value = update

def printState(code, res):
  print(res["update"])

device.data().get("state", initializeState)
device.data().on("state", updateState)

# Runs the code forever (every 1 second), till the device reboots
while(1):
  state = not led.value
  device.data().set("state", state, printState)
  # Waits for a second
  sleep(1)

```

### Test it With Your Web app

You can build a web app for your product to control your hardware device over Grandeur.

## The Dexterity of Py SDK

The Py SDK is aimed at providing extremely to-the-point functions, being almost invisible in your device program to make the integration of Grandeur in your product seamless. Here is what it does under the hood without you paying attention to the most painful things:

* **Py SDK** takes care of your device's connection to [Grandeur](https://grandeur.tech/). **It can start trying to connect with Grandeur as soon as you call `grandeur.init` with the proper credentials.** When it connects, only then does the communication with Grandeur happen. And if somehow the connection breaks, SDK handles the reconnection and everything resumes right from where it left.

*  **Py SDK** exposes the state of your device (`CONNECTED` or `DISCONNECTED`) through [`isConnected()`](#isconnected) function to let you make your decisions based on that.

* **Py SDK** is event-driven. You can set **event handler** for device's connection or disconnection with Grandeur by using [`onConnection()`](#onconnection). So, when the device connects or disconnects from Grandeur, the function passed to `onConnection()` is called.

* You can also set **update handlers** for device's sdata using [`on()`](#on). So, when the any of the device variables is updated, the function passed to `on()` is called.

* **Async functions** are what make the event-drive of the SDK possible. They do all the same things as regular functions plus one extra. They receive a function parameter which they schedule for later. 

To see the **Py SDK** in action, jump to [Example](#example).

# Grandeur Ecosystem

The purpose of writing this is to give you a glimpse into the thought process and psychologies behind designing the Grandeur Platform the way it feels now. We believe that the first very important step towards choosing a platform for your product and company is to understand the design language of developers of the platform. So we thought of writing about it in detail. We wanted to document how you can use this platform effectively to make your life as a developer or founder a bit simpler.

Here we present a case study to help you understand exactly where, how and what Grandeur can help you with. Then we explain some of the terms and keywords we use to identify and classify things that make abstraction seamless. So here we go.

## A Brief Case Study

Suppose you are a cleantech startup and want to radicalize the home appliances market to make the appliances more eco and user friendly. You analyzed the market, did user interviews and realized that there is a really big problem in the air conditioner market. Even though millions of new air conditioners are produced every year but there are so many old and inefficient ACs already in the market installed in people's homes and offices. These old air conditioners consume a huge chunk of power and are a major cause of CFCs emissions. Something has to be done because these devices are impacting both the users and the environment. Upgrading each single one of them is just not feasible at all economically.

To resolve the energy efficiency issue of these old ACs, you decided to build an electronic solution that could be used as an extension with these old ACs. So people could control their power consumption without actually upgrading their devices. And you thought of providing your users with an interface to interact with their appliances. You wanted your users to see how much has this new extension been saving them in expenses by cutting down the power consumption. You also wanted to give your users control over how much they wanted to save through this app. In short, you decided to make your product smart (on IoT). And you decided to build a companion app for your device.

That's where the problem arose. You are a hardware startup, after all, that builds amazing electronics technology. But here you got to deal with a few more things as well. You have to build your app and figure out how to establish its communication with your hardware. You may decide to hire more engineers. But do you know how much of them will you have to hire? To give you a perspective, you generally need 8+ engineers just to do the server-end, like one to figure out your networking, one to design and manage your database, one to develop your API (the interface layer between your users and devices), about four for building your SDKs (one for each platform android, ios, web, and hardware) and then when you start scaling up a bit, one DevOps engineer. This makes it a package of $8000+ just to figure out the backend of your system and you haven't even validated your product yet. This turns out exhausting for your business. You have hit a concrete wall with no idea what to do about it.

Then one day the sun of fate shown. You came across a platform that goes by the name of Grandeur. You went through its [website](https://grandeur.tech/) and discovered a perfectly fitting solution for all your headaches. You wanted a solution for authentication of your users, it has the Auth feature in it. You needed online file storage to store maybe the profile pictures of your users and other stuff, it comes with a storage builtin. You were in dire need of a scalable out-of-the-box database to store power consumption logs of your device to show your users graphs on their monthly/yearly savings, it provides a cloud datastore service. And the most important of these all, you needed a realtime communication bridge between your hardware and your apps, THANK GOD, its SDKs are available for all the stacks including Arduino, web, and mobile (both android and ios).

So here you are giving it a shot. You simply [registered for the platform](https://cloud.grandeur.tech/), created your first project, downloaded their SDKs and started connecting your devices and apps through Grandeur. You didn't even have to worry about the security of your users and devices, because the data on Grandeur is protected under standard security protocols. Each user and device in a project is limited in its scope. All you had to worry about was designing your product core and develop your business logic. And in a matter of weeks, your product was out in people's hands, your apps live on app stores. People loved what you built and you were getting live feedback on it. You could see how many people have paired with your devices. You made an early entry into the market and now adding a dent to the universe.

By the way, that is the story of team SolDrive. Check out their [website](http://sol-drive.com/) right now and explore how they are transforming the world with Grandeur.

## Concepts

In this subsection, we will explore the Grandeur platform in detail and see how it pulls it all off. So let's get started.

### Project

A project is the first thing you need to create to start working with Grandeur. A project is like a namespace, a completely isolated network of users and devices, along with separate file storage and a separate datastore. While you can create an unlimited number of projects, but no two projects can interact or share anything with one other.

Each project is identified by a digital signature that we call the API key, just as your identification card or social security number identifies you as a citizen. To connect your apps or hardware to your project's network, this is what you need to provide to the SDKs. The API key is sent with every request to Grandeur and this is what defines the project of the request. Check out the [SDK](#sdk) section to read more about it.

> ***NOTE***: Our pricing applies separately to each project. So you get a free tier on every project and pay for each separately for what you consume when you cross your resources limit.

### SDK

Grandeur is the API that exposes Grandeur to the outside world. Our SDKs utilize this API and map each functionality to a function. We have tried our best to make the integration of our SDKs into your codebase simple. For example, while developing your web app, you simply need to drop in the link of JS SDK CDN in your codebase and you are done. We have developed our SDKs for each platform in coherence with each other so you could work and collaborate everywhere seamlessly.

This is how they work: In every SDK, there is a global object aka. `grandeur`. You can initialize your configurations (API Key and a couple of more stuff in case of hardware SDK) by calling `grandeur.init()`. This returns you a reference to your whole project (in case of your app) or just to your device (in case of hardware because hardware scope is limited to the device itself). In **JS SDK**, you can interact with the authentication API, the device API, the file storage and the datastore API. In the case of **Py SDK** your scope is limited to just the device's namespace. Check out the [Authentication and Access](#authentication-and-access) section to get more insight into how scope varies across the different platforms (app and hardware).

### User and Administrator

This topic is about the relationship between you as an administrator and your users and the access scope of both.

You aka. **the administrator** is an entity that creates, develops and maintains one or more [projects](#project) on Grandeur. The administrator has full authority over a project's resources (users, devices, files, and data) and can monitor and control all its projects from the [dashboard](https://cloud.grandeur.tech/dashboard).

A **user** is an entity that uses your product. While you have full control over your project, a user of your product has access to his profile and delegated access limited to its device scope only.

In the real world, you would not want to add a new user or pair a device with that user manually every time someone buys your product. Therefore you delegate a part of your project authorities to the SDK when you plug your project's API Key in. And so a new user gets to sign up, pair, monitor and control your device through your product's companion app.

Using just your project's API Key for full delegation is like putting all of your eggs in one basket. A stolen API Key can give the hacker, at the minimum, user-level access to your project. He can register any number of bogus users and do whatnot. Hence the concept of CORS comes to play. Read more on CORS in [Allowed Origins](#allowed-origins) section.

### Device

Devices are the *things* in **Internet of Things** (IoT) around which the IoT product development revolves. Like a user, a device entity has a limited scope of access. But unlike users, you can register new devices only from the dashboard. Read the [Device Registry](#device-registry) section for more on what happens when you register a new device to your project.

On Grandeur, a device falls under the ownership of the project's administrator. The project's API Key delegates the device pairing authority to the SDK which the user uses to pair with the device. Pairing a device makes it live on Grandeur and the user gets delegated access to the device's data. But a user cannot delete or modify a device's inherent data because it's not within its scope.

A user can pair with any number of devices but a device can be paired with at the most one user.

The device entity, in the end, defines two things:

* What kind of data a hardware device can access in your namespace and
* Which hardware devices a user can control.

This matters a lot because you would never want your neighbor to control your air conditioner (that would be a horrible situation). That's what this entity has been designed for. A user can only interact with devices that are paired with it.

When you pair a device with a user account, an access token is generated for the device. This token is what the device uses to connect to Grandeur. This token also delegates access of the device namespace to the Py SDK. The Py SDK takes this access token along with the project's API Key while doing `grandeur.init()`. To read about the device's namespace and how the device's data is stored on Grandeur, have a look at the [Device Registry](#device-registry) section.

> ***NOTE***: A user cannot pair with a device that is already paired.

### Device Registry

The device registry constitutes one of the key elements of Grandeur. There are two types of approaches you see out there:

* Those which deal with user's authentication only e.g. firebase and
* Those which employ a device's registry e.g. Google IoT Core, to make sure no unauthorized devices get into your network.

We wanted to combine the best of both worlds. This is why at Grandeur, not do we just authenticate a device on connection, we also maintain a device's registry for you. See [Authentication and Access](#authentication-and-access) section for detail on how a device is authenticated on Grandeur.

When you register a device, you make it available in your project's network. Not just that, a new namespace is created for your device in the device registry. When your device comes online, this is where all of its data is stored.

We defined these two objects just to give you a basic framework to work on and build your logic fast. But we are very flexible in what and how you store data in the device registry. You can define an initial schema of these objects using models and go on from there.

### Authentication and Access

Previously, we have discussed in depth which entity (administrator, user, device) can access what. This section revisits the topic and gives you a broader picture of authentication and access scopes. Let's start by outlining the relationships. There are three major scopes:

* The global scope or project's scope
* User scope
* Device scope

You (as an administrator) create a project and therefore have global access to everything. You can access and manage your projects and their resources using the dashboard application. You want your users and devices to have limited access to your project's resources based on their scopes which you achieve by using our SDKs in your apps and hardware. Your project's API Key delegates your project's access to the SDKs and access tokens allow and limit, at the same time, this access to user and device scopes.

The user scope is wider than the device scope. A user can access its profile, the registry of the devices it's paired to, the files in the project's storage and the data in the project's datastore. When a user logs in, an Auth token is returned. This token along with the API Key, being sent with every request, is what validates the authority of the request.

The device scope is limited to the device's namespace in the device registry. When a user pairs with a device, an access token is returned for the device. This access token along with the API Key is what authenticates the device's connection to Grandeur.

This is how the global project scope is distributed among the smaller entities and we make sure that everyone gets what they are allowed to access.

### Networking

Here we write about how the networking works on Grandeur.

We work with two communication channels in **Web SDK** i) HTTP based REST API channel and ii) Duplex based realtime API channel. We use the first to do some basic things like authentication or handle big requests like file uploading, while the latter, as its name suggests, for realtime communication like fetching or updating the device's data. The realtime channel is as fast as 200ms RTT. It is based on our custom protocol aka. Duplex. We do not allow any unauthenticated communication over this channel and therefore authenticate a connection over the REST channel first.

In the **Py SDK**, we only use the realtime channel. A device cannot establish a connection over this channel unless and until its access token is validated. A device access token is provided while initializing the grandeur configurations through `grandeur.init()`.

### Allowed Origins

This is another amazing topic and somehow related to access delegation in the end. As mentioned in the sections above that you can interact with your project's namespace through the JS SDK by initializing grandeur with your API key. This returns an object referring to your project which can be used to interact with its resources including its devices, datastore, and files storage. Putting this much responsibility on just the API key poses a security threat particularly in case of web apps as API Key can easily be stolen. Even though a user needs to log in first before making any request to Grandeur, a hacker with having your API key can still cause some serious damage. For example, Registering bogus users to your project or creating a copycat site on your name for phishing to name a few. That's where cross-origin request sharing (CORS) policies come to play.

So to allow a web app to interact with your project using the Web SDK, you first need to whitelist the domain name your web app uses via the settings page in the dashboard. You cannot even send a request from your localhost without first whitelisting it.

> ***NOTE***: Keeping localhost whitelisted in a production application is a very serious vulnerability that can make you pay as you go (pun intended).

# Documentation

A `Project` reference refers to your project on Grandeur, has the widest scope in Py SDK, and all functionalities originate from it. You get it when you initialize SDK's configurations using `grandeur.init()`.

### init

> grandeur.init (apiKey: _String_, token: _String_) : returns _Project_

This method initializes SDK's connection configurations: `apiKey` and `authToken`, and returns a reference to Grandeur `Project`. This `Project` reference lies at the widest scope and exposes all functions of the SDK.

#### Parameters

| Name        | Description                                                     |
|-------------|-----------------------------------------------------------------|
| apiKey      | API key of your project that your device belongs to             |
| token       | Access token generated when the device is paired with the user  |

#### Example

```py
import grandeur.device as grandeur

grandeur.init(ApiKey, DeviceToken)

// **RESULT**
// SDK configurations are initialized.

```

## Project

`Project` is the main class and all functionalities originate from it. You can safely imagine the object of `Project` class as a reference to your project on Grandeur. You get a reference to this object when you initialize SDK's configurations using `grandeur.init()`.

`grandeur` is the global object that gets available right away when you include the package in your code. It has just one purpose and therefore gives you only one function: `grandeur.init()`.

### init

> grandeur.init (apiKey: str, token: str) -> Project

This method initializes SDK's connection configurations: `apiKey` and `authToken`, and returns a reference to object of the `Project` class. `Project` class is the main class that exposes all functions of the SDK.

#### Parameters

| Name        | Type     | Description                                                     |
|-------------|----------|-----------------------------------------------------------------|
| apiKey      | _String_ | API key of your project that your device belongs to             |
| token       | _String_ | Access token generated when the device is paired with the user  |

#### Example

```python
import grandeur.device as grandeur

# Init the sdk
project = grandeur.init(APIKey, Token)

// **RESULT**
// SDK configurations are initialized.
```

## Project

Project is the main class of the SDK. When SDK connects with Grandeur, this class represents your cloud project, tuned down to the device scope. There are only two APIs you can interact with: device and datastore, which are represented by their respective classes.

This class exposes the following methods:

### isConnected

> isConnected(): -> bool

This method returns true if the SDK is connected with Grandeur.

#### Example

```python
import grandeur.device as grandeur

# Init the sdk
project = grandeur.init(APIKey, Token)

# ....
# Check connection status
print(project.isConnected())

// **RESULT**
// Returns the conenction status
```

### onConnection

> onConnection(callback: Callable[[str], None]) -> None

This method schedules a function to be called when the SDK's connection with Grandeur is made or broken. The function passed to it as argument is called an **event handler** for it handles events like connection/disconnection with Cloud. Example below illustrates its usage.

#### Parameters

| Name        | Type             | Description                                                                    |
|-------------|------------------|--------------------------------------------------------------------------------|
| callback    | Callable[[str], None] | An event handler function for device's connection/disconnection with Grandeur  |


#### Example

```python
import grandeur.device as grandeur

# Init the sdk
project = grandeur.init(APIKey, Token)

# Function to handle connection state
def connectionHandler(state):
  print(state)

# Add listener to connection state
project.onConnection(connectionHandler)
```

### device

> device (deviceID: str) -> Device

This method returns a reference to object of the **Device** class.

#### Example

```python
import grandeur.device as grandeur

# Init the sdk
project = grandeur.init(APIKey, Token)

# Get reference to device class
device = project.device(DeviceID)
```

## Device

Device class exposes the functions of the device API. Its data function returns a reference to object of `Data` class which represents device's data space. You can use it to update device variables on Grandeur, pulling variables from Grandeur, listening for updates in your device variables, etc.

Device's `Data` class exposes the following functions:

### get

> get(path: str, callback: Callable[[str, dict], None]) -> None

This method gets a device variable from Grandeur.

#### Parameters

| Name        | Type       | Description                                                  |
|-------------|------------|--------------------------------------------------------------|
| path        | str   | Path of the device variable using dot notation            |
| callback    | Callable[[str, dict], None] | A function to be called when get response is received        |

#### Example

```python
import grandeur.device as grandeur

# Init the sdk
project = grandeur.init(APIKey, Token)

# Get reference to device class
device = project.device(DeviceID)

# Function to handle the response on get call
def getCallback(code, res):
  print(res["data"])

# Get data of the device
device.data().get("", getCallback)
```

### set

> set(path: str, data: dict, callback: Callable[[str, dict], None]) ->  None

This method updates a device variable on Grandeur with new data.

#### Parameters

| Name        | Type          | Description                                                  |
|-------------|---------------|--------------------------------------------------------------|
| path        | str      | Path of the device variable using dot notation               |
| data        | dict         | New data to store in the variable                            |
| callback    | Callable[[str, dict], None]    | A function to be called when set response is received        |

#### Example

```python
import grandeur.device as grandeur

# Init the sdk
project = grandeur.init(APIKey, Token)

# Get reference to device class
device = project.device(DeviceID)

# Function to handle the response on get call
def setCallback(code, res):
  print(res["update"])

# Store new data in a dict
data = {"state": 0}

# Get data of the device
device.data().set("", data, setCallback)
```

### on

> on(path: str, callback: Callable[[str, dict], None]) -> Subscriber

This method schedules a function to be called when a device variable changes on Grandeur.

> ***A Tidbit***: *Update is a special type of event* and the function that handles it is called an **update handler**.

#### Parameters

| Name        | Type       | Description                                    |
|-------------|------------|------------------------------------------------|
| path        | str   | Path of the device variable using dot notation |
| callback    | Callable[[str, dict], None] | An update handler for the device variable      |

#### Example

```python
import grandeur.device as grandeur

# Init the sdk
project = grandeur.init(APIKey, Token)

# Get reference to device class
device = project.device(DeviceID)

# Function to handle the update from server
def updateHandler(path, update):
  print(update)

# Get data of the device
device.data().on("", updateHandler)
```
