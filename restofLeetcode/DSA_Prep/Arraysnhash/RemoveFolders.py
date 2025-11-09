"""
The idea here is that we remove all subdirectories and only return the parent directories
"""

class Solution(object):
    def removeSubfolders(self, folder):
        folder.sort(key=len)
        result = set()
        for dir in folder:
            dir_parts = dir.split('/')
            parent_dir = ''
            for part in dir_parts[1:]:
                parent_dir += "/" + part
                if parent_dir in result:
                    break
            else:
                result.add(parent_dir)
        return list(result)