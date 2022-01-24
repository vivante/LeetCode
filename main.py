import sys

import multiprocessing as mp

from leetcode_api import LeetCodeAPI

if __name__ == "__main__":
  leetcode_api = LeetCodeAPI(sys.argv)
  pool = mp.Pool(mp.cpu_count())
  pool.apply(leetcode_api.write_problems)
  pool.close()
  leetcode_api.write_mkdocs()
  leetcode_api.write_readme()
