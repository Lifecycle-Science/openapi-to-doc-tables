---
id: get-get-user-actions
title: "ActionHub | Get User Actions"
description: "Get a list recommended actions for a given user. _Growth actions_ are weighted by expected impact. Higher weights means greater expected impact. _Base weights_ reflect the influence of the action on the growth calculations based on past engagement."
---
# Get User Actions
<code class='method-name'><span class='get'>GET</span> /users/{'{user_id}'}/actions</code>

Get a list recommended actions for a given user. _Growth actions_ are weighted by expected impact. Higher weights means greater expected impact. _Base weights_ reflect the influence of the action on the growth calculations based on past engagement.

## Request Parameters 

### Path Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>user_id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>


### Query Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>limit</code></td><td>integer</td><td>

Default: 10<br/>Number of actions to be returned in result

</td></tr><tr><td><code>allow_repeats</code></td><td>boolean</td><td>

Default: True<br/>Include actions already taken? Default is true (1)

</td></tr></table>


### Header Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>program-id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>

## Responses  

### `200` Successful Response

UserNextActionList | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>actions</code> <span class='required'>required</span></td><td>array</td><td>

items: {'$ref': '#/components/schemas/UserNextAction'}<br/>
</td></tr></table>

UserNextAction | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>event_type</code> <span class='required'>required</span></td><td>string</td><td>

description: The behavior recommended in the action<br/>
</td></tr><tr><td><code>asset_id</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>asset_name</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>growth_weight</code> <span class='required'>required</span></td><td>number</td><td>

description: The strength of the action recommendation for the given user. Higher values mean stronger recommendation.<br/>
</td></tr><tr><td><code>base_weight</code> <span class='required'>required</span></td><td>number</td><td>

description: The historical weight of the action for the given user, accounting for recency and frequency. Higher values mean greater impact on the recommendations. *NOTE: exclude values > 0 to recommend new actions only* <br/>
</td></tr></table>


**Response Example**  

```json
{
  "actions": [
    {
      "event_type": "string",
      "asset_id": "string",
      "asset_name": "string",
      "growth_weight": "number",
      "base_weight": "number"
    }
  ]
}
```

### `404` User history not found

ErrorMessage | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>detail</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr></table>


### `422` Validation Error

HTTPValidationError | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>detail</code></td><td>array</td><td>

items: {'$ref': '#/components/schemas/ValidationError'}<br/>
</td></tr></table>

ValidationError | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>loc</code> <span class='required'>required</span></td><td>array</td><td>

items: {'anyOf': [{'type': 'string'}, {'type': 'integer'}]}<br/>
</td></tr><tr><td><code>msg</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>type</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr></table>

