# Bank voice assistant app

### How to run project

Requirements: pre-installed json-server and rasa.

1. Train model `rasa train`
2. Start json-server `json-server fake_server/db.json`
3. Start rasa actions `rasa run actions --port 8000`
4. Start testing mode `rasa shell`


How to run project in google action app

1. Select port. For example 5005.
2. Run command `./ngrok http 5005`
3. Copy ngrok https address and add it into action.json with suffix `/webhooks/google_assistant/webhook`
4. Start rasa server with command `rasa run --enable-api -p 5005`
5. Start json-server with command `json-server fake_server/db.json`
6. Run rasa actions `rasa run actions`
7. Start google action test session `./gactions.dms test --action_package action.json --project bank-client-2505b`
