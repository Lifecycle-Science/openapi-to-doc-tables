---
id: post-post-events
title: "ActionHub | Post Events"
description: "Add events to the event store. When `process_user_actions=true` new events will trigger updates to user action recommendations and label weights."
---
# Post Events
<code class='method-name'><span class='post'>POST</span> /events</code>

Add events to the event store. When `process_user_actions=true` new events will trigger updates to user action recommendations and label weights.

## Request Parameters 

### Query Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>queue_updates</code></td><td>boolean</td><td>

Default: False<br/>- `true` (default) : Process user updates in background, very fast response (ack) - `false` : Process user updates and produce new action recommendations immediately, slightly longer response time, guaranteed user update 

</td></tr><tr><td><code>process_user_actions</code></td><td>boolean</td><td>

Default: True<br/>- `true` (default) : Process updated action recommendations for event users. Use this option for real-time event logging and action feedback - `false` : Do not process updated action recommendations for event users. Use this option for bulk loading or back-filling a large number of events 

</td></tr></table>


### Header Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>program-id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>

## Request Body  

EventList | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>events</code> <span class='required'>required</span></td><td>array</td><td>

items: {'$ref': '#/components/schemas/Event'}<br/>description: Array of events, from minimum of 1 event to maximum 1000 events<br/>
</td></tr></table>

Event | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>user_id</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>event_timestamp</code> <span class='required'>required</span></td><td>string</td><td>

description: Time the event occurred in ISO 8601 format<br/>format: date-time<br/>
</td></tr><tr><td><code>event_type</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>asset_id</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>labels</code> <span class='required'>required</span></td><td>array</td><td>

items: {}<br/>description: Array of labels associated with instance of the event. These should not be used as asset labels which should be managed separately.<br/>
</td></tr></table>


**Request Example**  

```json
{
  "events": [
    {
      "user_id": "string",
      "event_timestamp": "string",
      "event_type": "string",
      "asset_id": "string",
      "labels": "array"
    }
  ]
}
```

## Responses  

### `200` Successful Response

SuccessMessage | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>result</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr></table>


**Response Example**  

```json
{
  "result": "string"
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

