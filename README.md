# Grandeur [![Version](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://cloud.grandeur.tech)

Building a smart (IoT) product is an art because it is about unifying the physical world with the digital one. When you put a piece of hardware on the web, magic happens. But one device on the web is one thing. Think about tens of them, interconnected, forging an automated ecosystem of pure reverie. Now imagine tens of thousands of these ecosystems spread throughout the globe. Seems profound, no? But developing an IoT product and then managing it is just as profoundly difficult. It involves development across a huge technology stack (your IoT hardware itself, your apps to monitor/control your hardware and a server backend to manage them both) to make such products work in production. And then in production comes the hardest challenge; you are going to have to scale it up as your user base grows.

We understand this because we have been there.

Introducing Grandeur: A backend as a service (Baas) platform for IoT. We have designed this platform so you do not have to worry about the backend of your next big thing, and can focus on what matters the most: your hardware and your apps. It is designed specifically to accelerate your IoT product development and push your products to market in weeks rather than in months or years. So you can then actually build *grandeur* ecosystems like the one above.

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

* Simple pricing. Unlike Google and AWS, we do not have to deal with a different pricing model for each service and aggregate them together to compute the monthly bill making it almost impossible for the user to understand why he has to pay this much! Packaging all our services into one platform has let us develop a very simple and transparent pricing model. You can [start free][Grandeur Sign Up] for a certain quota and then pay as you go based on your resources consumption. Checkout [pricing][Grandeur Pricing] for more details.

* We have a growing [community on Hackster][Grandeur Hackster] which is equivalent to growing number of developers which are using Grandeur and improving the opensource SDKs resulting in increasing Grandeur support.

* It is terrifically simple to [get started][Get Started with Grandeur] with your IoT product development. Just create a project from the [cloud dashboard][Grandeur Dashboard], plug your project's API key into our SDKs and start developing.

Follow [our Hackster Hub][Grandeur Hackster] for quick starts and advanced development projects.

[Here][Get Started With Grandeur] is how you can create a new project on Grandeur and start using the Javascript SDK to build your IoT apps.

From here onwards, we'll look at how you can use the Py SDK for all arduino-compatible modules to put your devices live and connected on Grandeur. Let's dive in!

# Py SDK

**Py SDK** is the official SDK for Linux-based Raspberry Pis and SoCs and it utilizes the *Grandeur* API to connect your device to **[Grandeur][Grandeur]**.

Follow the [get started][Get Started with Py SDK] guidelines to quickly get into the context of integrating your devices to Grandeur or jump straight to an [Py example][Example] to make your hands dirty.

For a developer reference for the Py SDK, you can have a look at the [documentation][Documentation].

To get a deeper understanding of the core concepts Grandeur is built upon, dive into the [Grandeur Ecosystem][Ecosystem] section.

* [Get Started](#get-started)
  * [Installation](#installation)
  * [Inclusion](#inclusion)
  * [Initialization](#initialization)
  * [Handling the WiFi](#handling-the-wifi)
  * [Setting Up the Valve](#setting-up-the-valve)
  * [Events Listening](#events-listening)
  * [Fetching Device Variables and Updating Them](#fetching-device-variables-and-updating-them)
  * [Handling Updates From the Cloud](#handling-updates-from-the-cloud)
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
    * [loop](#loop)
    * [device](#device)
    * [datastore](#datastore)
  * [Device](#device)
    * [getSummary](#getsummary)
    * [getParms](#getparms)
    * [setSummary](#setsummary)
    * [setParms](#setparms)
    * [onSummary](#onsummary)
    * [onParms](#onparms)
  * [Datastore](#datastore)
    * [insert](#insert)
* [Enhancements Under Consideration](#enhancements-under-consideration)

## Get Started

### Installation

1. You can install **Py SDK** using python's **pip**.
```sh
pip install grandeur
```

2. You can also clone **Py SDK** from [here][Py SDK].

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
project = grandeur.init(YourApiKey, YourDeviceToken)

# **RESULT**
# Initializes the SDK's configurations and returns your project reference.
```

As soon as you call `grandeur.init()`, the SDK uses the configurations to start trying to connect with the your project on the Cloud.

### Setting Up Connection Event Handler

You can also listen on SDK's connection-related events. For example, to run some code when the device makes a successful connection to the cloud or when the device's connection to the cloud breaks, you can wrap that code in a function and pass it to `Project`'s `onConnection()` function.

Here's how you can handle the connection event:

```py
import grandeur.device as grandeur

# Init the SDK and get reference to the project
project = grandeur.init(YourApiKey, YourDeviceToken)

# This method handles the events related to device's connection with the Cloud.
def onConnection(state):
    # Prints the current state
    print(state)

# Setting up listener for device's connection event
project.onConnection(onConnection)

# **RESULT**
# Prints CONNECTED when device gets connected to the cloud.
# And prints DISCONNECTED when device's connection from
# the cloud breaks.
```

### Fetching Device Variables and Updating Them

On Grandeur, we generally store the device data in two containers: **summary** to contain uncontrollable device variables and **parms** to contain controllable device variables. You can get and set both types using the following functions of the `Device` class:

* `myDevice.getSummary()`
* `myDevice.getParms()`
* `myDevice.setSummary()`
* `myDevice.setParms()`

They are all **Async functions** because they communicate with the Cloud through internet. Communication through internet takes some time and we cannot wait, for example, for device's summary variables to arrive from the Cloud — meanwhile blocking the rest of the device program. So, what we do is, we schedule a function to be called when the summary variables and resume with rest of the device program, forgetting that we ever called `getSummary()`. When the summary variables arrive, the SDK calls our scheduled function, giving us access to summary variables inside that function.

Read more about **Async functions** and `Callback` [here][the dexterity of Py SDK].

Here's how we would get and set device's summary and parms:

```py
import grandeur.device as grandeur

# This method handles the events related to device's connection with the Cloud.
def onConnection(state):
    # Prints the current state
    print(state)

# This function prints the variables stored in summary
def getSummaryCallback(data):
    print(data["deviceSummary"])

# This function prints the variables stored in parms
def getParmsCallback(data):
    print(data["deviceParms"])

# This function prints the updated values of the variables stored in summary
def setSummaryCallback(data):
    print(data["update"])

# This function prints the updated values of the variables stored in parms
def setParmsCallback(data):
    print(data["update"])

# Init the SDK and get reference to the project
project = grandeur.init(YourApiKey, YourDeviceToken)

# Setting up listener for device's connection event
project.onConnection(onConnection)

# Get a reference to our device
device = project.device(YourDeviceID)

# Getting device's summary
device.getSummary(getSummaryCallback)
# Getting device's parms
device.getParms(getParmsCallback)

# Setting device's summary
summary = {"voltage": 220, "current": 10}
device.setSummary(summary, setSummaryCallback)
# Setting device's parms
parms = {"state": 0}
device.setParms(parms, setParmsCallback)

# **RESULT**
# Summary and parms are fetched first. When they arrive from the cloud, their
# corresponding callbacks are called which print the variables stored in summary and parms objects.
# Then the summary and parms are updated with the new values. When their updates complete, their
# callbacks are called with the updated values of their variables and these updated values are
# printed on the screen.
```

### Handling Updates From the Cloud

Device variables are distributed on the cloud in **summary** and **parms** containers. Passing a method to `onSummary()` and `onParms()` you can set **update handlers** for updates to those variables. Let's do that now:

```py
import grandeur.device as grandeur

# This method handles the events related to device's connection with the Cloud.
def onConnection(state):
    # Prints the current state
    print(state)

# This function prints the updated values of the variables stored in summary
def summaryUpdatedCallback(updatedSummary):
    print(updatedSummary["voltage"], updatedSummary["current"])

# This function prints the updated values of the variables stored in parms
def parmsUpdatedCallback(updatedParms):
    print(updatedParms["state"])

# Init the SDK and get reference to the project
project = grandeur.init(YourApiKey, YourDeviceToken)

# Setting up listener for device's connection event
project.onConnection(onConnection)

# Get a reference to our device
device = project.device(YourDeviceID)

# Setting update handler for summary variables
device.onSummary(summaryUpdatedCallback)
# Setting update handler for parms variables
device.onParms(parmsUpdatedCallback)

# **RESULT**
# Whenever an update in the device's summary or parms occur, the updated values of the
# variables are printed.
```

## Example

Here we go through a general example of a Raspberry Pi to explain the **Py SDK** in action. For a little more broken-down approach, do have a look at [these examples][Examples] as well.

To begin working with the **Py SDK**, the very first step is to [create a new project][Grandeur Dashboard] and [register a new device][Grandeur Devices] through the [Cloud Dashboard][Grandeur Dashboard]. Then create a new python environment to keep your workspace packages isolated from the rest of the packages.

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

project = grandeur.init(YourAPIKey, YourToken)
```

You can find the API Key on the [settings page][Grandeur Settings] of your project's dashboard. For the Access Token, you need to pair your device with a user account in your project first. A device can only connect to Grandeur if it's paired with a user. And only the paired user can access the device's data through its web app. For convenient testing, we have made device pairing function available on the [devices page][Grandeur Devices] too. You can find your device's ID and pair your device with a user account. If your project has no registered user yet, you can add one easily from the [accounts page][Grandeur Accounts].

### Initialize Your Device

Before doing anything, you need to initialize your device with data from the cloud to keep your device running in undefined states when it first starts. You can get all the device variables by using `getSummary()` and `getParms()` methods of the device. Here's how you can get the device **state** from the cloud and initialize RPi's pin — we'll use the gpiozero package to interact with RPi's GPIOs for that.

```py
import grandeur.device as grandeur
from gpiozero import LED

# Selecting GPIO 17 to update the state of
led = LED(17)

project = grandeur.init(YourAPIKey, YourToken)
device = project.device(YourDeviceID)

def initializeState(parms):
  print(parms["state"])
  led.value = parms["state"]

device.getParms(printParms)

```

### Set Update Handlers

Update handlers are the functions which are called when a device variable is updated on the cloud. The update could be from a user or the device itself. Without the handlers, your device would not be notified when a user turns it off from the webapp.
Here's how you can set update handlers in your sketch for the device's state stored in parms.

```py
import grandeur.device as grandeur
from gpiozero import LED

# Selecting GPIO 17 to update the state of
led = LED(17)

project = grandeur.init(YourAPIKey, YourToken)
device = project.device(YourDeviceID)

def initializeState(data):
  print(data["deviceParms"]["state"])
  led.value = data["deviceParms"]["state"]

def updateState(updatedParms):
  print(updatedParms["state"])
  led.value = updatedParms["state"]

device.getParms(initializeState)
device.onParms(updateState)

```

### Update Device Variables

To see the live state of the device on the web app, you need to keep sending the updated state after every few seconds. Since we've stored the device's state in **Parms**, we'll use the `setParms()` function to update the state value.

```py
import grandeur.device as grandeur
from gpiozero import LED

# Selecting GPIO 17 to update the state of
led = LED(17)

project = grandeur.init(YourAPIKey, YourToken)
device = project.device(YourDeviceID)

def initializeState(data):
  print(data["deviceParms"]["state"])
  led.value = data["deviceParms"]["state"]

def updateState(updatedParms):
  print(updatedParms["state"])
  led.value = updatedParms["state"]

def printState(data):
  print(data["update"]["state"])

device.getParms(initializeState)
device.onParms(updateState)

# Runs the code forever (every 1 second), till the device reboots
while(1):
  parms = {"state": not led.value}
  device.setParms(parms, printState)
  # Waits for a second
  sleep(1)

```

### Test it With Your Web app

You can build a web app for your product to control your hardware device over the cloud. [Here's a simple example for that][An Example Webapp].

## The Dexterity of Py SDK

The Py SDK is aimed at providing extremely to-the-point functions, being almost invisible in your device program to make the integration of Grandeur in your product seamless. Here is what it does under the hood without you paying attention to the most painful things:

* **Py SDK** takes care of your device's connection to [Grandeur][Grandeur]. **It can start trying to connect with the Cloud as soon as you call `grandeur.init` with the proper credentials.** When it connects, only then does the communication with Grandeur happen. And if somehow the connection breaks, SDK handles the reconnection and everything resumes right from where it left.

*  **Py SDK** exposes the state of your device (`CONNECTED` or `DISCONNECTED`) through [`getState()`][getState] function to let you make your decisions based on that.

* **Py SDK** is event-driven. You can set **event handler** for device's connection or disconnection with Grandeur by using [`onConnection()`][onConnection]. So, when the device connects or disconnects from the cloud, the function passed to `onConnection()` is called.

* You can also set **update handlers** for device's summary and parms using [`onSummary()`][onSummary] and [`onParms()`][onParms]. So, when the any of the device variables stored in summary or parms is updated, the function passed to `onSummary()` or `onParmsUpdated()` is called.

* **Async functions** are what make the event-drive of the SDK possible. They do all the same things as regular functions plus one extra. They receive a function parameter which they schedule for later. For example, in the device functionality, all of the following are Async functions:
  
  * `onConnection(Callback callback)`
  * `onSummary(Callback callback)`
  * `onParmsUpdated(Callback callback)`
  * `getSummary(Callback callback)`
  * `getParms(Callback callback)`
  * `setSummary(JSONObject summary, Callback callback)`
  * `setParms(JSONObject parms, Callback callback)`

  `getParms()` for example, requests the cloud for the device's parms and schedules a function for when the parms arrive, because obviously, they don't arrive instantaneously; there is always some latency involved in web communications.

To see the **Py SDK** in action, jump to [Example][Example].

# Grandeur Ecosystem

The purpose of writing this is to give you a glimpse into the thought process and psychologies behind designing the Grandeur Platform the way it feels now. We believe that the first very important step towards choosing a platform for your product and company is to understand the design language of developers of the platform. So we thought of writing about it in detail. We wanted to document how you can use this platform effectively to make your life as a developer or founder a bit simpler.

Here we present a case study to help you understand exactly where, how and what Grandeur can help you with. Then we explain some of the terms and keywords we use to identify and classify things that make abstraction seamless. So here we go.

## A Brief Case Study

Suppose you are a cleantech startup and want to radicalize the home appliances market to make the appliances more eco and user friendly. You analyzed the market, did user interviews and realized that there is a really big problem in the air conditioner market. Even though millions of new air conditioners are produced every year but there are so many old and inefficient ACs already in the market installed in people's homes and offices. These old air conditioners consume a huge chunk of power and are a major cause of CFCs emissions. Something has to be done because these devices are impacting both the users and the environment. Upgrading each single one of them is just not feasible at all economically.

To resolve the energy efficiency issue of these old ACs, you decided to build an electronic solution that could be used as an extension with these old ACs. So people could control their power consumption without actually upgrading their devices. And you thought of providing your users with an interface to interact with their appliances. You wanted your users to see how much has this new extension been saving them in expenses by cutting down the power consumption. You also wanted to give your users control over how much they wanted to save through this app. In short, you decided to make your product smart (on IoT). And you decided to build a companion app for your device.

That's where the problem arose. You are a hardware startup, after all, that builds amazing electronics technology. But here you got to deal with a few more things as well. You have to build your app and figure out how to establish its communication with your hardware. You may decide to hire more engineers. But do you know how much of them will you have to hire? To give you a perspective, you generally need 8+ engineers just to do the server-end, like one to figure out your networking, one to design and manage your database, one to develop your API (the interface layer between your users and devices), about four for building your SDKs (one for each platform android, ios, web, and hardware) and then when you start scaling up a bit, one DevOps engineer. This makes it a package of $8000+ just to figure out the backend of your system and you haven't even validated your product yet. This turns out exhausting for your business. You have hit a concrete wall with no idea what to do about it.

Then one day the sun of fate shown. You came across a platform that goes by the name of Grandeur. You went through its [website][Grandeur Technologies] and discovered a perfectly fitting solution for all your headaches. You wanted a solution for authentication of your users, it has the Auth feature in it. You needed online file storage to store maybe the profile pictures of your users and other stuff, it comes with a storage builtin. You were in dire need of a scalable out-of-the-box database to store power consumption logs of your device to show your users graphs on their monthly/yearly savings, it provides a cloud datastore service. And the most important of these all, you needed a realtime communication bridge between your hardware and your apps, THANK GOD, its SDKs are available for all the stacks including Arduino, web, and mobile (both android and ios).

So here you are giving it a shot. You simply [registered for the platform][Grandeur], created your first project, downloaded their SDKs and started connecting your devices and apps through Grandeur. You didn't even have to worry about the security of your users and devices, because the data on Grandeur is protected under standard security protocols. Each user and device in a project is limited in its scope. All you had to worry about was designing your product core and develop your business logic. And in a matter of weeks, your product was out in people's hands, your apps live on app stores. People loved what you built and you were getting live feedback on it. You could see how many people have paired with your devices. You made an early entry into the market and now adding a dent to the universe.

By the way, that is the story of team SolDrive. Check out their [website][SolDrive] right now and explore how they are transforming the world with Grandeur.

## Concepts

In this subsection, we will explore the Grandeur platform in detail and see how it pulls it all off. So let's get started.

### Project

A project is the first thing you need to create to start working with Grandeur. A project is like a namespace, a completely isolated network of users and devices, along with separate file storage and a separate datastore. While you can create an unlimited number of projects, but no two projects can interact or share anything with one other.

Each project is identified by a digital signature that we call the API key, just as your identification card or social security number identifies you as a citizen. To connect your apps or hardware to your project's network, this is what you need to provide to the SDKs. The API key is sent with every request to Grandeur and this is what defines the project of the request. Check out the [SDK][SDK] section to read more about it.

> ***NOTE***: Our pricing applies separately to each project. So you get a free tier on every project and pay for each separately for what you consume when you cross your resources limit.

### SDK

Grandeur is the API that exposes Grandeur to the outside world. Our SDKs utilize this API and map each functionality to a function. We have tried our best to make the integration of our SDKs into your codebase simple. For example, while developing your web app, you simply need to drop in the link of JS SDK CDN in your codebase and you are done. We have developed our SDKs for each platform in coherence with each other so you could work and collaborate everywhere seamlessly.

This is how they work: In every SDK, there is a global object aka. `grandeur`. You can initialize your configurations (API Key and a couple of more stuff in case of hardware SDK) by calling `grandeur.init()`. This returns you a reference to your whole project (in case of your app) or just to your device (in case of hardware because hardware scope is limited to the device itself). In **JS SDK**, you can interact with the authentication API, the device API, the file storage and the datastore API. In the case of **Py SDK** your scope is limited to just the device's namespace. Check out the [Authentication and Access][Authentication and Access] section to get more insight into how scope varies across the different platforms (app and hardware).

### User and Administrator

This topic is about the relationship between you as an administrator and your users and the access scope of both.

You aka. **the administrator** is an entity that creates, develops and maintains one or more [projects][Project] on Grandeur. The administrator has full authority over a project's resources (users, devices, files, and data) and can monitor and control all its projects from the [dashboard][Grandeur Dashboard].

A **user** is an entity that uses your product. While you have full control over your project, a user of your product has access to his profile and delegated access limited to its device scope only.

In the real world, you would not want to add a new user or pair a device with that user manually every time someone buys your product. Therefore you delegate a part of your project authorities to the SDK when you plug your project's API Key in. And so a new user gets to sign up, pair, monitor and control your device through your product's companion app.

Using just your project's API Key for full delegation is like putting all of your eggs in one basket. A stolen API Key can give the hacker, at the minimum, user-level access to your project. He can register any number of bogus users and do whatnot. Hence the concept of CORS comes to play. Read more on CORS in [Allowed Origins][Allowed Origins] section.

### Device

Devices are the *things* in **Internet of Things** (IoT) around which the IoT product development revolves. Like a user, a device entity has a limited scope of access. But unlike users, you can register new devices only from the dashboard. Read the [Device Registry][Device Registry] section for more on what happens when you register a new device to your project.

On Grandeur, a device falls under the ownership of the project's administrator. The project's API Key delegates the device pairing authority to the SDK which the user uses to pair with the device. Pairing a device makes it live on Grandeur and the user gets delegated access to the device's data. But a user cannot delete or modify a device's inherent data because it's not within its scope.

A user can pair with any number of devices but a device can be paired with at the most one user.

The device entity, in the end, defines two things:

* What kind of data a hardware device can access in your namespace and
* Which hardware devices a user can control.

This matters a lot because you would never want your neighbor to control your air conditioner (that would be a horrible situation). That's what this entity has been designed for. A user can only interact with devices that are paired with it.

When you pair a device with a user account, an access token is generated for the device. This token is what the device uses to connect to Grandeur. This token also delegates access of the device namespace to the Py SDK. The Py SDK takes this access token along with the project's API Key while doing `grandeur.init()`. To read about the device's namespace and how the device's data is stored on Grandeur, have a look at the [Device Registry][Device Registry] section.

> ***NOTE***: A user cannot pair with a device that is already paired.

### Device Registry

The device registry constitutes one of the key elements of Grandeur. There are two types of approaches you see out there:

* Those which deal with user's authentication only e.g. firebase and
* Those which employ a device's registry e.g. Google IoT Core, to make sure no unauthorized devices get into your network.

We wanted to combine the best of both worlds. This is why at Grandeur, not do we just authenticate a device on connection, we also maintain a device's registry for you. See [Authentication and Access][Authentication and Access] section for detail on how a device is authenticated on Grandeur.

When you register a device, you make it available in your project's network. Not just that, a new namespace is created for your device in the device registry. When your device comes online, this is where all of its data is stored, in the form of i) Summary and ii) Parms.

Now let's define what you can store in **Parms** and **Summary**. To be honest, there is no hard and fast rule about it. We just created two objects instead of a single one to help you develop understanding. However, we generally take the *parms as the directly controllable device variables* and the *summary as those device variables which are not directly controllable* or are just needed to be logged or displayed to apps. In another way, the parms sometimes refer to the inputs from the user and the summary refers to the outputs of the device resulting from the inputs. Consider an example where you have a smart light bulb. The parms can store the bulb ON/OFF state which the user can control, while in summary, you can log the voltage consumption of the bulb.

We defined these two objects just to give you a basic framework to work on and build your logic fast. But we are very flexible in what and how you store data in the device registry. You can define an initial schema of these objects using [models][models] and go on from there.

### Models

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

This is another amazing topic and somehow related to access delegation in the end. As mentioned in the sections above that you can interact with your project's namespace through the JS SDK by initializing grandeur with your API key. This returns an object referring to your project which can be used to interact with its resources including its devices, datastore, and files storage. Putting this much responsibility on just the API key poses a security threat particularly in case of web apps as API Key can easily be stolen. Even though a user needs to log in first before making any request to the cloud, a hacker with having your API key can still cause some serious damage. For example, Registering bogus users to your project or creating a copycat site on your name for phishing to name a few. That's where cross-origin request sharing (CORS) policies come to play.

So to allow a web app to interact with your project using the Web SDK, you first need to whitelist the domain name your web app uses via the settings page in the dashboard. You cannot even send a request from your localhost without first whitelisting it.

> ***NOTE***: Keeping localhost whitelisted in a production application is a very serious vulnerability that can make you pay as you go (pun intended).

# Documentation

A `Project` reference refers to your project on Grandeur, has the widest scope in Py SDK, and all functionalities originate from it. You get it when you initialize SDK's configurations using `grandeur.init()`.

### init

> grandeur.init (apiKey: _String_, token: _String_) : returns _Project_

This method initializes SDK's connection configurations: `apiKey` and `authToken`, and returns a reference to the Cloud `Project`. This `Project` reference lies at the widest scope and exposes all functions of the SDK.

#### Parameters

| Name        | Description                                                     |
|-------------|-----------------------------------------------------------------|
| apiKey      | API key of your project that your device belongs to             |
| token       | Access token generated when the device is paired with the user  |

#### Example

```py
import grandeur.device as grandeur

grandeur.init(YourAPIKey, YourDeviceToken)

// **RESULT**
// SDK configurations are initialized.

```

## Project

Project is the main class of the SDK. When SDK connects with the Cloud, this class represents your cloud project. Devices in this project and this project's datastore lie as subclasses of the Project class.

This class exposes the following methods:

### isConnected

> isConnected(): returns _Boolean_

This method returns true if the SDK is connected with Grandeur.

#### Example

```py
import grandeur.device as grandeur

project = grandeur.init(YourApiKey, YourToken)

while(1):
  if not project.isConnected():
    print("Device is not connected with the Cloud!\n")
  }
  else:
    print("Yay! Device has made a successful connection with Grandeur!")

  sleep(1)

// **RESULT**
// In the beginning, isConnected() returns false and the first *if-block* runs.
// When the SDK is connected with the Cloud, isConnected() returns true running the second
// *if-block*.
```

[Grandeur Technologies]: https://grandeur.tech "Grandeur Technologies"
[Grandeur]: https://cloud.grandeur.tech "Grandeur"
[Grandeur Sign Up]: https://cloud.grandeur.tech/register "Sign up on Grandeur"
[Grandeur Dashboard]: https://cloud.grandeur.tech/dashboard "Grandeur Dashboard"
[Grandeur Accounts]: https://cloud.grandeur.tech/accounts "Grandeur Accounts"
[Grandeur Devices]: https://cloud.grandeur.tech/devices "Grandeur Devices"
[Grandeur Settings]: https://cloud.grandeur.tech/settings "Grandeur Settings"
[Grandeur Pricing]: https://grandeur.tech/pricing "Pricing"
[Get Started With Grandeur]: https://github.com/grandeurtech/js-sdk#get-started "Get Started With Grandeur"
[An Example Webapp]: https://github.com/grandeurtech/js-sdk#example "An Example Webapp"
[Examples]:  https://github.com/grandeurtech/py-sdk/tree/master/examples/

[Grandeur Hackster]: https://www.hackster.io/grandeur "Hackster Community"

[Installation]: #installation "Installation"
[Example]: #example "Py SDK Example"
[Documentation]: #documentation "Documentation"
[Ecosystem]: #grandeur-ecosystem "Grandeur Ecosystem"

[SolDrive]: https://sol-drive.com/ "SolDrive"

[Project]: #project "Project"
[SDK]: #sdk "SDK"
[Authentication and Access]: #authentication-and-access "Authentication and Access"
[Allowed Origins]: #allowed-origins "Allowed Origins"
[Device Registry]: #device-registry "Device Registry"

[Get Started with Py SDK]: #get-started "Get Started with Py SDK"
[Py SDK]: https://github.com/grandeurtech/py-sdk "Py SDK"
[project]: #project "Project"
[summary]: #device-registry "Summary"
[parms]: #device-registry "Parms"
[the dexterity of Py SDK]: #the-dexterity-of-py-sdk "The Dexterity of Py SDK"
[models]: #models "Models"
[apikey]: #project "Project"
[access token]: #authentication-and-access "Authentication and Access"

[getState]: #get-state
[onConnection]: #grandeur-connection-event-listener
[onSummary]: #onSummary
[onParms]: #onParms
