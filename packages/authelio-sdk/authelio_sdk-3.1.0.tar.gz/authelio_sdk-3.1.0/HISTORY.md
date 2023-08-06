# Release history

### 3.1.0

- User `create` method updates:
  - A new optional parameter `auth_type` introduced. Parameter allows to specify user authentication type.
  - Mandatory parameter `username` change into an optional one. The Authelio API does not allowed to 
  specify `username` for the user of `federated_sso` auth type.

### 3.0.1

- Limit urllib3 dependency up to the breaking version.

### 3.0.0

- `user_ids` as arguments for the client `User` method `get` introduced.
- `group_ids` as arguments for the client `Group` methods `get` and `users` introduced. 

### 2.0.0

- New method `users` for the client `Group` added. The method retrieves either user IDs
  for the given group or common user ids for the given groups.
- Client `User` updates:
    - Method `filter` updated. Method accepts optional pagination parameters, `count` and
      next page token `page_id`. Returns chunk of filtered user entities and next page token
      if such exist.
    - Method `get` updated. Retrieval of multiple user entities implemented.
- Client `Group` updates:
    - Method `filter` updated. Method accepts optional pagination parameters, `count` and
      next page token `page_id`. Returns chunk of filtered group entities and next page token
      if such exist.
    - Method `get` updated. Retrieval of multiple group entities implemented.

### 1.1.0

- User login method returning hosted login page URL added.

### 0.0.5

- User filter method updated to include directly assigned user permissions.
- Redundant integration tests removed.

### 0.0.4

- SDK client base updated by introducing basic auth.

### 0.0.3

- Fix mismatched environment variable names in the pipeline.

### 0.0.2

- Add integration tests.

### 0.0.1

- Initial build.
