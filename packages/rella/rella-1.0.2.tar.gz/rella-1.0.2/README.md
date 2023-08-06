# Rella

---

This is the [Rella](https://rella.so) python SDK, allowing you to easily track what's happening in your Python applications.

### Installation

---

To install:

```
pip install rella
```

### Useage

---

```js
# Define the instance
from rella import Rella

rella = Rella(
    api_key="<your apiKey",
    enabled=True
)


# In your functions
rella.track(
        event_type="user-registered",
        title="User Registered",
        msg="Bobby Jones has registered",
        icon="🎉",
        color="#D1FADF",
        tags={
            "email": "bobby@tables.com",
            "userID": "1"
        }
)
```

You can also use the event builder located [here](https://app.rella.so/event-builder) to quickly prototype new events and generate the above python code automatically.
