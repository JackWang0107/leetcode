from typing import *
class Solution:
    # 56 ms, faster than 44.11% of Python3 online submissions for Subdomain Visit Count.
    # 14.2 MB, less than 91.54% of Python3 online submissions for Subdomain Visit Count.
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import defaultdict
        domain_dict = defaultdict(int)
        ans = []
        for paired_domain in cpdomains:
            visit, domain = paired_domain.split(" ")
            subdomain = domain.split(".")
            for i in range(len(subdomain)):
                domain_dict[".".join(subdomain[i:])] += int(visit)
        for key, value in domain_dict.items():
            ans.append(f"{value} {key}")
        return ans


if __name__ == "__main__":
    so = Solution()
    print(so.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))