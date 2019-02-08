# iotlabclient.client
REST API documentation of [IoT-LAB](http://www.iot-lab.info) testbed.

The `iotlabclient.client` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.15
* six >= 1.10
* certifi
* python-dateutil

## Getting Started

In your own code, to use this library to connect and interact with iotlabclient.client,
you can run the following:

```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint

configuration = iotlabclient.client.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = iotlabclient.client.DefaultApi(iotlabclient.client.ApiClient(configuration))
firmware = '/path/to/file' # file | firmware binary file (optional)

try:
    # Returns firwmare format.
    api_response = api_instance.get_firmware_format(firmware=firmware)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_firmware_format: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://www.iot-lab.info/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**get_firmware_format**](iotlabclient/client/docs/DefaultApi.md#get_firmware_format) | **POST** /firmwares/checker | Returns firwmare format.
*ExperimentApi* | [**experiments_id_get**](iotlabclient/client/docs/ExperimentApi.md#experiments_id_get) | **GET** /experiments/{id} | Returns experiment.
*ExperimentApi* | [**experiments_id_nodes_flash_name_post**](iotlabclient/client/docs/ExperimentApi.md#experiments_id_nodes_flash_name_post) | **POST** /experiments/{id}/nodes/flash/{name} | Send experiment nodes flash firmware store command.
*ExperimentApi* | [**experiments_id_token_get**](iotlabclient/client/docs/ExperimentApi.md#experiments_id_token_get) | **GET** /experiments/{id}/token | Returns experiment websocket token.
*ExperimentApi* | [**get_experiment_archive**](iotlabclient/client/docs/ExperimentApi.md#get_experiment_archive) | **GET** /experiments/{id}/data | Returns experiment archive.
*ExperimentApi* | [**get_experiment_deployment**](iotlabclient/client/docs/ExperimentApi.md#get_experiment_deployment) | **GET** /experiments/{id}/deployment | Returns experiment deployment result.
*ExperimentApi* | [**get_experiment_nodes**](iotlabclient/client/docs/ExperimentApi.md#get_experiment_nodes) | **GET** /experiments/{id}/nodes | Returns experiment nodes list.
*ExperimentApi* | [**get_experiment_nodes_id**](iotlabclient/client/docs/ExperimentApi.md#get_experiment_nodes_id) | **GET** /experiments/{id}/nodes_ids | Returns experiment nodes id list (eg. 1-5+8).
*ExperimentApi* | [**kill_experiment_scripts**](iotlabclient/client/docs/ExperimentApi.md#kill_experiment_scripts) | **POST** /experiments/{id}/scripts/kill | Send frontend SSH kill script command.
*ExperimentApi* | [**reload_experiment**](iotlabclient/client/docs/ExperimentApi.md#reload_experiment) | **POST** /experiments/{id}/reload | Reload experiment.
*ExperimentApi* | [**run_experiment_scripts**](iotlabclient/client/docs/ExperimentApi.md#run_experiment_scripts) | **POST** /experiments/{id}/scripts/run | Send frontend SSH run script command
*ExperimentApi* | [**send_cmd_mobility_robots**](iotlabclient/client/docs/ExperimentApi.md#send_cmd_mobility_robots) | **POST** /experiments/{id}/robots/mobility/{name} | Send update robots mobility.
*ExperimentApi* | [**send_cmd_nodes**](iotlabclient/client/docs/ExperimentApi.md#send_cmd_nodes) | **POST** /experiments/{id}/nodes/{cmd} | Send experiment nodes command.
*ExperimentApi* | [**send_cmd_profile_nodes**](iotlabclient/client/docs/ExperimentApi.md#send_cmd_profile_nodes) | **POST** /experiments/{id}/nodes/monitoring/{name} | Send experiment nodes update monitoring profile store command.
*ExperimentApi* | [**send_cmd_robots**](iotlabclient/client/docs/ExperimentApi.md#send_cmd_robots) | **POST** /experiments/{id}/robots/{cmd} | Returns robots status.
*ExperimentApi* | [**send_cmd_update_nodes**](iotlabclient/client/docs/ExperimentApi.md#send_cmd_update_nodes) | **POST** /experiments/{id}/nodes/flash | Send experiment nodes flash firmware command.
*ExperimentApi* | [**send_load_profile_nodes**](iotlabclient/client/docs/ExperimentApi.md#send_load_profile_nodes) | **POST** /experiments/{id}/nodes/monitoring | Send experiment nodes load monitoring profile command.
*ExperimentApi* | [**status_experiment_scripts**](iotlabclient/client/docs/ExperimentApi.md#status_experiment_scripts) | **POST** /experiments/{id}/scripts/status | Returns frontend SSH status script.
*ExperimentApi* | [**stop_experiment**](iotlabclient/client/docs/ExperimentApi.md#stop_experiment) | **DELETE** /experiments/{id} | Stop experiment
*ExperimentsApi* | [**get_experiments**](iotlabclient/client/docs/ExperimentsApi.md#get_experiments) | **GET** /experiments | Returns experiments list
*ExperimentsApi* | [**get_experiments_total**](iotlabclient/client/docs/ExperimentsApi.md#get_experiments_total) | **GET** /experiments/total | Returns total number of experiments
*ExperimentsApi* | [**get_running_experiments**](iotlabclient/client/docs/ExperimentsApi.md#get_running_experiments) | **GET** /experiments/running | Returns running testbed experiments list
*ExperimentsApi* | [**submit_experiment**](iotlabclient/client/docs/ExperimentsApi.md#submit_experiment) | **POST** /experiments | Submit an experiment
*FirmwaresApi* | [**firmwares_get**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_get) | **GET** /firmwares | get a list of stored user firmware metadatas
*FirmwaresApi* | [**firmwares_name_delete**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_name_delete) | **DELETE** /firmwares/{name} | Delete a user firmware
*FirmwaresApi* | [**firmwares_name_file_get**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_name_file_get) | **GET** /firmwares/{name}/file | get a stored user firmaware file
*FirmwaresApi* | [**firmwares_name_get**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_name_get) | **GET** /firmwares/{name} | get a stored user firmware metadata
*FirmwaresApi* | [**firmwares_name_put**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_name_put) | **PUT** /firmwares/{name} | modify a stored user firmware
*FirmwaresApi* | [**firmwares_post**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_post) | **POST** /firmwares | save a user firmware
*MobilitiesApi* | [**delete_user_mobility**](iotlabclient/client/docs/MobilitiesApi.md#delete_user_mobility) | **DELETE** /mobilities/circuits/{name} | Delete circuit mobility
*MobilitiesApi* | [**get_mobilities**](iotlabclient/client/docs/MobilitiesApi.md#get_mobilities) | **GET** /mobilities/circuits | Returns circuits list
*MobilitiesApi* | [**get_mobility**](iotlabclient/client/docs/MobilitiesApi.md#get_mobility) | **GET** /mobilities/circuits/{name} | Returns circuit
*MobilitiesApi* | [**modify_user_mobility**](iotlabclient/client/docs/MobilitiesApi.md#modify_user_mobility) | **PUT** /mobilities/circuits/{name} | Modify circuit mobility
*MobilitiesApi* | [**save_user_mobility**](iotlabclient/client/docs/MobilitiesApi.md#save_user_mobility) | **POST** /mobilities/circuits | Create circuit
*MonitoringApi* | [**delete_profile**](iotlabclient/client/docs/MonitoringApi.md#delete_profile) | **DELETE** /monitoring/{name} | Delete monitoring profile.
*MonitoringApi* | [**get_profile**](iotlabclient/client/docs/MonitoringApi.md#get_profile) | **GET** /monitoring/{name} | Returns monitoring profile.
*MonitoringApi* | [**get_profiles**](iotlabclient/client/docs/MonitoringApi.md#get_profiles) | **GET** /monitoring | Returns monitoring profiles list.
*MonitoringApi* | [**modify_profile**](iotlabclient/client/docs/MonitoringApi.md#modify_profile) | **PUT** /monitoring/{name} | Modify monitoring profile.
*MonitoringApi* | [**save_profile**](iotlabclient/client/docs/MonitoringApi.md#save_profile) | **POST** /monitoring | Create monitoring profile.
*NodesApi* | [**get_nodes**](iotlabclient/client/docs/NodesApi.md#get_nodes) | **GET** /nodes | Returns testbed nodes list.
*NodesApi* | [**get_nodes_id**](iotlabclient/client/docs/NodesApi.md#get_nodes_id) | **GET** /nodes/ids | Returns testbed nodes ids list (eg. 1-5+8).
*RobotsApi* | [**are_coordinates_reachable**](iotlabclient/client/docs/RobotsApi.md#are_coordinates_reachable) | **POST** /robots/{site}/coordinates/isreachable | Returns if robots coordinates (eg. ROS points) are reachable
*RobotsApi* | [**get_dock_config**](iotlabclient/client/docs/RobotsApi.md#get_dock_config) | **GET** /robots/{site}/dock/config | Returns robots site dock config
*RobotsApi* | [**get_map_config**](iotlabclient/client/docs/RobotsApi.md#get_map_config) | **GET** /robots/{site}/map/config | Returns robots site map config
*RobotsApi* | [**get_map_coordinates**](iotlabclient/client/docs/RobotsApi.md#get_map_coordinates) | **POST** /robots/{site}/coordinates/map | Returns robots map coordinates from ros coordinates.
*RobotsApi* | [**get_map_image**](iotlabclient/client/docs/RobotsApi.md#get_map_image) | **GET** /robots/{site}/map/image | Returns robots site map image
*RobotsApi* | [**get_ros_coordinates**](iotlabclient/client/docs/RobotsApi.md#get_ros_coordinates) | **POST** /robots/{site}/coordinates/ros | Returns robots ros coordinates from map coordinates.
*SitesApi* | [**get_sites**](iotlabclient/client/docs/SitesApi.md#get_sites) | **GET** /sites | Returns testbed sites list.
*SitesApi* | [**get_sites_details**](iotlabclient/client/docs/SitesApi.md#get_sites_details) | **GET** /sites/details | Returns tesbed sites details list.
*UsersApi* | [**activate_user**](iotlabclient/client/docs/UsersApi.md#activate_user) | **POST** /users/activate | Activate user.
*UsersApi* | [**delete_user**](iotlabclient/client/docs/UsersApi.md#delete_user) | **DELETE** /user | Delete user.
*UsersApi* | [**delete_user_ssh_keys**](iotlabclient/client/docs/UsersApi.md#delete_user_ssh_keys) | **DELETE** /user/keys/{id} | Delete user ssh key.
*UsersApi* | [**get_user**](iotlabclient/client/docs/UsersApi.md#get_user) | **GET** /user | Returns user
*UsersApi* | [**get_user_ssh_keys**](iotlabclient/client/docs/UsersApi.md#get_user_ssh_keys) | **GET** /user/keys | Returns user ssh keys list.
*UsersApi* | [**modify_user**](iotlabclient/client/docs/UsersApi.md#modify_user) | **PUT** /user | Modify user
*UsersApi* | [**reset_password**](iotlabclient/client/docs/UsersApi.md#reset_password) | **POST** /users/reset_password | Reset user password by email
*UsersApi* | [**set_user_ssh_keys**](iotlabclient/client/docs/UsersApi.md#set_user_ssh_keys) | **POST** /user/keys | Add user ssh keys.
*UsersApi* | [**update_password**](iotlabclient/client/docs/UsersApi.md#update_password) | **PUT** /user/password | Modify user password.
*UsersApi* | [**users_post**](iotlabclient/client/docs/UsersApi.md#users_post) | **POST** /users | Signup user.


## Documentation For Models

 - [ActivateUserRequest](iotlabclient/client/docs/ActivateUserRequest.md)
 - [Alias](iotlabclient/client/docs/Alias.md)
 - [AliasProperties](iotlabclient/client/docs/AliasProperties.md)
 - [Archi](iotlabclient/client/docs/Archi.md)
 - [Circuit](iotlabclient/client/docs/Circuit.md)
 - [CircuitsListResponse](iotlabclient/client/docs/CircuitsListResponse.md)
 - [CoordinatesReachable](iotlabclient/client/docs/CoordinatesReachable.md)
 - [CoordinatesReachableItems](iotlabclient/client/docs/CoordinatesReachableItems.md)
 - [Deployment](iotlabclient/client/docs/Deployment.md)
 - [DockConfig](iotlabclient/client/docs/DockConfig.md)
 - [Error](iotlabclient/client/docs/Error.md)
 - [ExperimentAlias](iotlabclient/client/docs/ExperimentAlias.md)
 - [ExperimentPhysical](iotlabclient/client/docs/ExperimentPhysical.md)
 - [ExperimentRequest](iotlabclient/client/docs/ExperimentRequest.md)
 - [ExperimentRequestMobilities](iotlabclient/client/docs/ExperimentRequestMobilities.md)
 - [ExperimentRequestProfiles](iotlabclient/client/docs/ExperimentRequestProfiles.md)
 - [ExperimentResponse](iotlabclient/client/docs/ExperimentResponse.md)
 - [ExperimentSubmission](iotlabclient/client/docs/ExperimentSubmission.md)
 - [ExperimentsResponse](iotlabclient/client/docs/ExperimentsResponse.md)
 - [Firmware](iotlabclient/client/docs/Firmware.md)
 - [FirmwareAliasAssociations](iotlabclient/client/docs/FirmwareAliasAssociations.md)
 - [FirmwareAliasAssociationsFirmwareassociations](iotlabclient/client/docs/FirmwareAliasAssociationsFirmwareassociations.md)
 - [FirmwareAssociations](iotlabclient/client/docs/FirmwareAssociations.md)
 - [FirmwareAssociationsFirmwareassociations](iotlabclient/client/docs/FirmwareAssociationsFirmwareassociations.md)
 - [InlineObject](iotlabclient/client/docs/InlineObject.md)
 - [InlineObject1](iotlabclient/client/docs/InlineObject1.md)
 - [InlineObject2](iotlabclient/client/docs/InlineObject2.md)
 - [InlineObject3](iotlabclient/client/docs/InlineObject3.md)
 - [InlineObject4](iotlabclient/client/docs/InlineObject4.md)
 - [InlineObject5](iotlabclient/client/docs/InlineObject5.md)
 - [InlineObject6](iotlabclient/client/docs/InlineObject6.md)
 - [InlineResponse200](iotlabclient/client/docs/InlineResponse200.md)
 - [InlineResponse2001](iotlabclient/client/docs/InlineResponse2001.md)
 - [InlineResponse2002](iotlabclient/client/docs/InlineResponse2002.md)
 - [InlineResponse2003](iotlabclient/client/docs/InlineResponse2003.md)
 - [MobilityAliasAssociations](iotlabclient/client/docs/MobilityAliasAssociations.md)
 - [MobilityAliasAssociationsMobilityassociations](iotlabclient/client/docs/MobilityAliasAssociationsMobilityassociations.md)
 - [MobilityAssociations](iotlabclient/client/docs/MobilityAssociations.md)
 - [Node](iotlabclient/client/docs/Node.md)
 - [NodesIdsResponse](iotlabclient/client/docs/NodesIdsResponse.md)
 - [NodesIdsResponseArchis](iotlabclient/client/docs/NodesIdsResponseArchis.md)
 - [NodesIdsResponseItems](iotlabclient/client/docs/NodesIdsResponseItems.md)
 - [NodesIdsResponseStates](iotlabclient/client/docs/NodesIdsResponseStates.md)
 - [NodesResponse](iotlabclient/client/docs/NodesResponse.md)
 - [Point](iotlabclient/client/docs/Point.md)
 - [Profile](iotlabclient/client/docs/Profile.md)
 - [ProfileAliasAssociations](iotlabclient/client/docs/ProfileAliasAssociations.md)
 - [ProfileAssociations](iotlabclient/client/docs/ProfileAssociations.md)
 - [ProfileAssociationsProfileassociations](iotlabclient/client/docs/ProfileAssociationsProfileassociations.md)
 - [ProfileConsumption](iotlabclient/client/docs/ProfileConsumption.md)
 - [ProfileRadio](iotlabclient/client/docs/ProfileRadio.md)
 - [Reload](iotlabclient/client/docs/Reload.md)
 - [ResetPasswordRequest](iotlabclient/client/docs/ResetPasswordRequest.md)
 - [RobotResponse](iotlabclient/client/docs/RobotResponse.md)
 - [RobotResponsePower](iotlabclient/client/docs/RobotResponsePower.md)
 - [RobotsDockConfig](iotlabclient/client/docs/RobotsDockConfig.md)
 - [RobotsMapConfig](iotlabclient/client/docs/RobotsMapConfig.md)
 - [RobotsStatusResponse](iotlabclient/client/docs/RobotsStatusResponse.md)
 - [ScriptAssociations](iotlabclient/client/docs/ScriptAssociations.md)
 - [ScriptAssociationsScript](iotlabclient/client/docs/ScriptAssociationsScript.md)
 - [ScriptAssociationsScriptconfig](iotlabclient/client/docs/ScriptAssociationsScriptconfig.md)
 - [Site](iotlabclient/client/docs/Site.md)
 - [SiteAssociations](iotlabclient/client/docs/SiteAssociations.md)
 - [SitesDetailsResponse](iotlabclient/client/docs/SitesDetailsResponse.md)
 - [SitesResponse](iotlabclient/client/docs/SitesResponse.md)
 - [SitesResponseItems](iotlabclient/client/docs/SitesResponseItems.md)
 - [StatusResponse](iotlabclient/client/docs/StatusResponse.md)
 - [StopResponse](iotlabclient/client/docs/StopResponse.md)
 - [TotalResponse](iotlabclient/client/docs/TotalResponse.md)
 - [UpdatePasswordRequest](iotlabclient/client/docs/UpdatePasswordRequest.md)
 - [UserRequest](iotlabclient/client/docs/UserRequest.md)
 - [UserResponse](iotlabclient/client/docs/UserResponse.md)
 - [UserSshKeys](iotlabclient/client/docs/UserSshKeys.md)


## Documentation For Authorization


## BasicAuth

- **Type**: HTTP basic authentication


## Author



