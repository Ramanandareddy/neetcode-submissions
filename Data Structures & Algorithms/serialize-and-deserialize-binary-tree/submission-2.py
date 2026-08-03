class Codec:

    def serialize(self, root):
        if not root:
            return "N"

        return (
            str(root.val) + "," +
            self.serialize(root.left) + "," +
            self.serialize(root.right)
        )

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()