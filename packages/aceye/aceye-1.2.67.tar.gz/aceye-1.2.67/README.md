[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/automateyournetwork/ACEye)

# ACEye

Business Ready Documents for Cisco ACI

## Current API Coverage

Access Bundle Groups

Access Control Entities

Access Control Instances

Access Control Rules

Access Control Scope

Access Port Groups

Access Port Profiles

Application Profiles

ARP Adjacency Endpoints

ARP Database

ARP Domain

ARP Entity

ARP Instances

ARP Interfaces

Attachable Access Entity Profiles

*Audit Log

BGP Address Families

BGP Domains

BGP Entities

BGP Instances

BGP Instances Policy

BGP Peers

BGP Peers AF Entries

BGP Peers Entries

BGP Route Reflector Policy

BGP Route Reflectors

Bridge Domains

Bridge Domains Target Relationships

Bridge Domains To Outside

CDP Adjacency Endpoints

CDP Entities

CDP Instances

CDP Interface Addresses

CDP Interfaces

CDP Management Addresses

Cluster Aggregate Interfaces

Cluster Health

Cluster Physical Interfaces

Cluster RS Member Interfaces

Compute Controllers

Compute Domains

Compute Endpoint Policy Descriptions

Compute Providers

Compute RS Domain Policies

Context Source Relationships

Contexts (VRFs)

Contexts Target Relationships

Contracts

Contract Consumer Interfaces

Contract Consumers

Contract Providers

Contract Subjects

Controllers

Device Packages

Domain Attachments

Endpoint Profile Containers

Endpoints (All Connected Fabric Endpoints)

Endpoints To Paths

EPG to Bridge Domain Links

EPGs (Endpoint Groups)

Equipment Board Slots

Equipment Boards

Equipment Chassis

Equipment CPUs

Equipment DIMMs

Equipment Fabric Extenders

Equipment Fabric Ports

Equipment Fan Slots

Equipment Fan Trays

Equipment Fans

Equipment Field Programmable Gate Arrays

Equipment Indicator LEDs

Equipment Leaf Ports

Equipment Line Card Slots

Equipment Line Cards

Equipment Port Locator LEDs

Equipment Power Supplies

Equipment Power Supply Slots

Equipment RS IO Port Physical Configs

Equipment Sensors

Equipment SP Common Blocks

Equipment SPROM LCs

Equipment SPROM Power Supplies

Equipment SPROM Power Supply Blocks

Equipment SPROM Supervisors

Equipment Storage

Equipment Supervisor Slots

Equipment Supervisors

Ethernet Port Manager Physical Interfaces

*Events

Fabric Extended Path Endpoint Containers

Fabric Instances

Fabric Link Containers

Fabric Links

Fabric Loose Links

Fabric Loose Nodes

Fabric Membership

Fabric Node SSL Certifcates

Fabric Nodes

Fabric Path Endpoint Containers

Fabric Path Endpoints

Fabric Paths

Fabric Pods

Fabric Protected Path Endpoint Containers

Fault Summary

FEX Policies

Fibre Channel Entity

Filters

Firmware Card Running

Firmware Compute Running

Firmware Running

Function Policies

Health

Host Port Selectors

Interface Policies

Interface Profiles

IP Addresses

License Entitlements

L2Outs

L3 Domains

L3 Interfaces

L3Outs

Leaf Interface Profiles

Leaf Switch Profiles

Locales

Path Attachments

Physical Domains

Physical Interfaces

Port Blocks

Prefix List

Prefix List Detailed

QOS Classes

Security Domains

Spine Interface Profiles

Spine Switch Profiles

Subnets

Tenant

Tenant Health

Top System

Users

VLAN Encapsulation Blocks

VLAN Namespace Policies

VLAN Pools

* Both Audit Log and Events are commented out of the base package due to the potentially huge number of records; should you want the Audit Log / Events please uncomment out lines 72-73 (Audit Log) and 76-77 (Events)


## Installation

```console
$ python3 -m venv ACI
$ source ACI/bin/activate
(ACI) $ pip install aceye
```

## Usage - Help

```console
(ACI) $ aceye --help
```

![ACEye Help](/images/help.png)

## Usage - In-line

```console
(ACI) $ aceye --url <url to APIC> --username <APIC username> --password <APIC password>
```

## Usage - Interactive

```console
(ACI) $ aceye
APIC URL: <URL to APIC>
APIC Username: <APIC Username>
APIC Password: <APIC Password>
```

## Usage - Environment Variables

```console
(ACI) $ export URL=<URL to APIC>
(ACI) $ export USERNAME=<APIC Username>
(ACI) $ export PASSWORD=<APIC Password>
```

## Recommended VS Code Extensions

Excel Viewer - CSV Files

Markdown Preview - Markdown Files

Markmap - Mindmap Files

Open in Default Browser - HTML Files

## Contact

Please contact John Capobianco if you need any assistance
