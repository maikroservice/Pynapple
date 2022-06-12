#
# This file holds all configurations for the crawler.
#


worker_count = 8

# Search parameters for the GitHub API
# github_repo_query = 'stars:75..150 pushed:>2017-01-08 size:<=10000'
search_params = {
    "stars": (75, 150),
    "last_accessed": "2017-01-08",
    "max_size": 10000,
}

PROCESSES_BASE_DIR = "processed"
LOGS_BASE_DIR = "logs"
TMP_BASE_DIR = "tmp"
GITHUB_TOKEN_FNAME = "github_token.txt"
PLUGIN_BASE_DIR = "plugins"

"""
configs = {c["name"]: SimpleNamespace(**c) for c in (
    patterns.php_sql_config,
    patterns.php_simple_sql_config,
    patterns.node_sql_config,
    patterns.java_sql_config,
    patterns.php_xss_config,
    patterns.js_xss_config,
    patterns.bo_cpp_config,
    patterns.bo_cpp_strcpy_config
)}
"""