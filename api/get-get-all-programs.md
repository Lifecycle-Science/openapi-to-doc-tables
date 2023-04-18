---
id: get-get-all-programs
title: "ActionHub | Get All Programs"
description: "Get a list of programs available to the supplied API key."
---
# Get All Programs
<code class='method-name'><span class='get'>GET</span> /programs</code>

Get a list of programs available to the supplied API key.

## Request Parameters 

### Header Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>program-id</code></td><td>string</td><td>



</td></tr></table>

## Responses  

### `200` Successful Response

ProgramList | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>programs</code> <span class='required'>required</span></td><td>array</td><td>

items: {'$ref': '#/components/schemas/Program'}<br/>
</td></tr></table>

Program | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>program_id</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>program_name</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>high_engagement_threshold</code></td><td>integer</td><td>

description: This value is the number of actions establishing a user as 'highly engaged' (your best customers) for the purposes of inclusion in the engagement model.<br/>
</td></tr><tr><td><code>event_relevance_decay</code></td><td>integer</td><td>

description: This value is the number of days for events to lose half their weight (also called event half-life), implemented as a decay curve over time. This value is used to account for recency relevance so newer actions can carry extra weight in calculations.
            <br/>
</td></tr><tr><td><code>action_weight_floor</code></td><td>number</td><td>

description: This value is the minimum user action recommendation weight required for the action to be included in the final recommendations. Higher numbers bring higher confidence in the recommendations but also limit the number of recommendations provided.<br/>
</td></tr><tr><td><code>description</code></td><td>string</td><td>


</td></tr></table>


**Response Example**  

```json
{
  "programs": [
    {
      "program_id": "string",
      "program_name": "string",
      "high_engagement_threshold": "integer",
      "event_relevance_decay": "integer",
      "action_weight_floor": "number",
      "description": "string"
    }
  ]
}
```

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

