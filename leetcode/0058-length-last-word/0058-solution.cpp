class Solution {
public:
    int lengthOfLastWord(string s) {
        
        int i{ static_cast<int>(s.size()) - 1 };

        while (i > 0 && s[i] == ' ')
        {
            i--;
        }

        int end{i};

        while (i >= 0 &&  s[i] != ' ')
        {
            i--;
        }

        return end - i;
    }
};
