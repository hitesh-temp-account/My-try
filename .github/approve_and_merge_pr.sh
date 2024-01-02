# take input
pr_number=$1
app_token=$2
github_token=$3


- name: Approve PR
  if: pr_number
  run: |
  gh pr review pr_number --approve
  echo "approved"
  env:
    GITHUB_TOKEN: app_token

- name: Turn On PR Auto-Merge
  id: auto-merge
  if: pr_number
  run: >
    gh pr merge --squash --auto 
    --repo ${{ github.repository }} --delete-branch
    pr_number
  env:
    GITHUB_TOKEN: github_token
