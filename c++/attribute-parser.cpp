#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>
#include <utility>
#include <string>

using namespace std;

string getWord(string::iterator &startWordIterator, string::iterator &endIterator)
{
    string word{};
    startWordIterator = find_if(startWordIterator, endIterator, [](char character)
                                { return character != ' ' && character != '=' && character != '\"' && character != '>' && character != '<' && character != '~'; });

    auto endWordIterator = find_if(startWordIterator, endIterator, [](char character)
                                   { return character == ' ' || character == '=' || character == '\"' || character == '>' || character == '<' || character == '~'; });

    if (startWordIterator == endIterator)
    {
        return "";
    }

    copy(startWordIterator, endWordIterator, back_inserter(word));

    startWordIterator = endWordIterator;
    return word;
}

map<string, string> getAttributesFromLineIterator(string::iterator &startWordIterator, string::iterator &endIterator)
{
    map<string, string> attributesAndValue{};
    string attribute, value;

    while ((attribute = getWord(startWordIterator, endIterator)) != "")
    {
        value = getWord(startWordIterator, endIterator);
        attributesAndValue[attribute] = value;
    }

    return attributesAndValue;
}

void findAndPrint(map<string, map<string, string>> &hrmlStructure, string &line)
{
    auto startWordIterator = line.begin();
    auto lineEndIterator = line.end();

    string tag, attribute;
    tag = getWord(startWordIterator, lineEndIterator);
    attribute = getWord(startWordIterator, lineEndIterator);

    auto tagIter = hrmlStructure.find(tag);
    if (tagIter == hrmlStructure.end())
    {
        cout << "Not Found!" << endl;
        return;
    }

    auto attribIter = (*tagIter).second.find(attribute);
    if (attribIter == (*tagIter).second.end())
    {
        cout << "Not Found!" << endl;
        return;
    }

    cout << (*attribIter).second << endl;
}

string getTagPathFromStack(vector<string> &tagStack)
{
    string tagPath{};
    auto tagIterator = tagStack.begin();
    tagPath.append(*tagIterator++);

    for (; tagIterator != tagStack.end(); ++tagIterator)
    {
        tagPath.push_back('.');
        tagPath.append(*tagIterator);
    }

    return tagPath;
}

int main()
{
    map<string, map<string, string>> hrmlStructure{};
    vector<string> tagStack{};
    string::iterator startWordIterator;
    string::iterator endWordIterator;

    int N{0}, Q{0};
    cin >> N >> Q;

    string line{};
    getline(cin, line);

    for (int i = 0; i < N; ++i)
    {
        getline(cin, line);

        startWordIterator = line.begin();
        endWordIterator = line.end();

        string tag = getWord(startWordIterator, endWordIterator);
        if (tag[0] == '/')
        {
            tagStack.pop_back();
        }
        else
        {
            map<string, string> attributes = getAttributesFromLineIterator(startWordIterator, endWordIterator);
            tagStack.push_back(tag);
            string tagPath = getTagPathFromStack(tagStack);
            hrmlStructure[tagPath] = attributes;
        }
    }

    for (int i = 0; i < Q; ++i)
    {
        getline(cin, line);
        findAndPrint(hrmlStructure, line);
    }

    return 0;
}
