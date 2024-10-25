class Solution(object):
    def removeSubfolders(self, folder):
        folder.sort()
        result = []
        prev_path = ""
        
        for path in folder:
            if not prev_path or not (path.startswith(prev_path + "/")):
                result.append(path)
                prev_path = path
                
        return result
    
test_cases = [
    ["/a","/a/b","/c/d","/c/d/e","/c/f"],
    ["/a","/a/b/c","/a/b/d"],
    ["/a/b/c","/a/b/ca","/a/b/d"],
    ["/a","/aa","/a/b","/aa/b"],
    ["/a"],
]

app = Solution()

for folders in test_cases:
    print(f"Input: {folders}")
    print(f"Output: {app.removeSubfolders(folders)}\n")