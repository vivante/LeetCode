import sys

from leetcode_api import LeetCodeAPI

if __name__ == "__main__":
  leetcode_api = LeetCodeAPI(sys.argv)
  leetcode_api.write_problems()
  leetcode_api.write_mkdocs()
  leetcode_api.write_readme()
