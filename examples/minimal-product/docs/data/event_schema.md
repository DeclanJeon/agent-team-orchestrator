# Event Schema

| Event | Trigger | Properties | Consumer |
|---|---|---|---|
| request_submitted | public form submit success | request_id, topic, timeframe, source | inbox metrics, ops |
| request_status_changed | owner updates status | request_id, previous_status, next_status | ops, growth |
