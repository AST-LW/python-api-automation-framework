#!/bin/bash

# Read the webhook URL from the environment variable
webhook_url="$DISCORD_WEBHOOK_URL"

# Exit if the DISCORD_WEBHOOK_URL is not set
if [ -z "$webhook_url" ]; then
    echo "DISCORD_WEBHOOK_URL environment variable is not set."
    exit 1
fi

# Read test summary from a JSON file
ROOT_DIR=${ROOT_DIR:-$(git rev-parse --show-toplevel)}
test_summary=$(cat $ROOT_DIR/test-summary.json)

# Extract properties using jq
total_passed=$(echo "$test_summary" | jq '.totalPassed')
total_failed=$(echo "$test_summary" | jq '.totalFailed')
total_broken=$(echo "$test_summary" | jq '.totalBroken')
env=$(echo "$test_summary" | jq -r '.env')
suite_name=$(echo "$test_summary" | jq -r '.suite')
total_duration=$(echo "$test_summary" | jq -r '.totalDuration')

# Use total duration directly
total_duration_formatted="$total_duration"

# Define the color based on the test results
message_color=3066993 # Green for success

# Define the message payload with embeds
message_payload=$(cat <<EOF
{
    "embeds": [
        {
            "title": "Test Summary: $suite_name Suite",
            "color": $message_color,
            "fields": [
                {
                    "name": "Environment",
                    "value": "$env",
                    "inline": true
                },
                {
                    "name": "Total Passed",
                    "value": "$total_passed",
                    "inline": true
                },
                {
                    "name": "Total Failed",
                    "value": "$total_failed",
                    "inline": true
                },
                {
                    "name": "Total Broken",
                    "value": "$total_broken",
                    "inline": true
                },
                {
                    "name": "Total Duration",
                    "value": "$total_duration_formatted",
                    "inline": true
                }
            ],
            "footer": {
                "text": "This summary provides an overview of the test outcomes from the latest $suite_name testing cycle."
            }
        }
    ]
}
EOF
)

# Send the message using curl
curl -X POST -H 'Content-type: application/json' --data "$message_payload" "$webhook_url"