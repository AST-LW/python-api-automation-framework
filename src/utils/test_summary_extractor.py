import os
import json
import glob


class StringOperations:
    @staticmethod
    def capitalize_first_letter(string):
        return string.capitalize()


def extract_allure_summary():
    summary = {
        "totalPassed": 0,
        "totalFailed": 0,
        "totalBroken": 0,
        "totalDurationMs": 0,
    }

    try:
        test_cases_path = os.path.join(
            os.getcwd(), "allure-report", "data", "test-cases")
        json_files = glob.glob(os.path.join(test_cases_path, "*.json"))

        for file_path in json_files:
            with open(file_path, "r", encoding="utf-8") as file:
                test_case = json.load(file)

                # Count pass/fail/broken statuses
                if test_case.get("status") == "passed":
                    summary["totalPassed"] += 1
                elif test_case.get("status") == "failed":
                    summary["totalFailed"] += 1
                elif test_case.get("status") == "broken":
                    summary["totalBroken"] += 1

        duration_trend_path = os.path.join(
            os.getcwd(), "allure-report", "history", "duration-trend.json")
        with open(duration_trend_path, "r", encoding="utf-8") as file:
            duration_trend = json.load(file)
            summary["totalDurationMs"] = duration_trend[0]["data"]["duration"]

        # Additional metadata
        summary["env"] = os.getenv("ENV")
        summary["suite"] = StringOperations.capitalize_first_letter(
            os.getenv("SUITE"))

        # Format the total duration into hours, minutes, and seconds
        summary["totalDuration"] = format_duration(summary["totalDurationMs"])
        # Remove the milliseconds duration from the summary
        del summary["totalDurationMs"]

    except Exception as error:
        print("Error reading test case files:", error)
        raise

    summary_path = os.path.join(os.getcwd(), "test-summary.json")
    print(os.path.isfile(summary_path))
    print(summary_path)
    with open(summary_path, "w+", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    return summary


def format_duration(duration_ms):
    seconds = duration_ms // 1000
    minutes = seconds // 60
    hours = minutes // 60

    seconds = seconds % 60
    minutes = minutes % 60
    hours = hours % 24

    hours_str = str(hours).zfill(2) + "h"
    minutes_str = str(minutes).zfill(2) + "m"
    seconds_str = str(seconds).zfill(2) + "s"

    return hours_str + "-" + minutes_str + "-" + seconds_str


if __name__ == "__main__":
    extract_allure_summary()
