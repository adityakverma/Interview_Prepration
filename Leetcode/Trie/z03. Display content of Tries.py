
# https://www.geeksforgeeks.org/trie-display-content/

# // function to display the content of Trie
# void display(struct TrieNode* root, char str[], int level)
# {
#     // If node is leaf node, it indiicates end
#     // of string, so a null charcter is added
#     // and string is displayed
#     if (isLeafNode(root))
#     {
#         str[level] = '\0';
#         cout << str << endl;
#     }
#
#     int i;
#     for (i = 0; i < alpha_size; i++)
#     {
#         // if NON NULL child is found
#         // add parent key to str and
#         // call the display function recursively
#         // for child node
#         if (root->children[i])
#         {
#             str[level] = i + 'a';
#             display(root->children[i], str, level + 1);
#         }
#     }
# }


