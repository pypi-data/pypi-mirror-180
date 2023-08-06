# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.5] - 2022-12-10
### Changed
- major overhaul of base components
- include medux-common package into main package to ease documentation
  - new Tabler based layout
  - rename `Settings` to `Preference` to avoid name clashes with Django
  - Preferences can provide icons
  - remove TenantSite, prefer Homepage
  - switch from TurboDjango to HTMX, to Unicorn, to Tetra framework, back to HTMX :-)
  - Change the way tenant is determined
  - improved ScopedSettings permission system
  - MenuItem supports disabled and view_name
  - add MenuSeparator
  - switch from django-unicorn to turbo-django
  - renamed TenantedSite model to TenantSite
  - introduce IDashboardURL plugin hook
  - many bugfixes
  - improved/corrected ScopedSettings
  - improved testing / +CI
  - refactor "Client" to "Tenant"
  - improved SettingsRegistry
  - TenantedSites model as base for Homepage, PrescriptionsSite etc.
  - improved models and helpers
  - move Client model to medux.common
  - introduce SettingsRegistry
  - basic abstract models for usage throughout MedUX/MedUX online
  - ScopedSettings framework

## [0.1.0] 
- switch from sockpuppet back to Unicorn
- implement Patient search

#### Breaking changes:
- New database struture. No migration path available.

## [0.0.4] 2021-07-30
- allow .env to be non-existent during development

## [0.0.3] 2021-07-29
- massive FHIR model updates, incl Patient, Organizations, Datapacks etc.
- +some fixtures
- fix PyPi package

## [0.0.2]
- fix pypi upload

## [0.0.1]
### Changed
- install script for deploying on *buntu
- First version with decentralized plugin architecture. GDAPS plugins are separated.