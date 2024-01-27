#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

const int NODE_MAX = 5000;

struct Node {
    int data;   // 현재 노드의 데이터
    Node* next; // 다음 노드를 가리키는 포인터

    Node(int data) : data(data), next(nullptr) {}
    // Node(int data): Node 구조체의 생성자를 정의, 매개변수 data를 받아서 새로운 노드를 초기화
    // data(data): 변수 data를 입력된 data 값으로 초기화
    // next(nullptr): 변수 next를 nullptr로 초기화
};

class LinkedList {
    Node* head; // 리스트의 처음을 가리키는 포인터
    Node* tail; // 리스트의 끝을 가리키는 포인터
    vector<Node*> nodeArr;  
    // Node 포인터를 담는 동적 배열인 vector 선언
    // 동적으로 크기가 조절되며 각 원소는 Node 구조체를 가리키는 포인터
    // nodeArr vector에는 Node 구조체를 가리키는 포인터들이 저장됨
    int nodeCnt;    // 생성된 노드 개수

public: // 클래스 외부에서 자유롭게 접근할 수 있도록 하는 접근 지정자
    LinkedList() : head(nullptr), tail(nullptr), nodeCnt(0) {
        nodeArr.resize(NODE_MAX, nullptr);
    }
    // head(nullptr), tail(nullptr): head, tail 멤버 변수를 nullptr로 초기화
    // nodeArr.resize(NODE_MAX, nullptr): nodeArr vector를 NODE_MAX 크기로 초기화

    Node* getNewNode(int data) {
        nodeArr[nodeCnt] = new Node(data);
        return nodeArr[nodeCnt++];
    }
    // 주어진 데이터를 가지는 새로운 노드를 생성하고 해당 노드의 포인터를 반환

    void insert(int idx, const vector<int>& nums) { 
        // idx: 삽입하려는 위치의 인덱스
        // const vector<int>& nums: 삽입할 노드들의 데이터를 담은 벡터, const는 함수 내에서 이 벡터를 수정하지 않음을 나타냄
        int st = 0;
        if (idx == 0) {
            if (head != nullptr) {  // 이미 리스트에 노드가 있는 경우
                Node* newNode = getNewNode(nums[0]);    // 새로운 노드를 생성하고 그 노드의 데이터를 nums[0]으로 설정
                newNode->next = head;   // 새로운 노드의 next를 head로 설정
                head = newNode;     // head 갱신
            }
            else {  // 리스트가 비어 있는 경우
                head = getNewNode(nums[0]); // 새로운 노드를 생성하고 이를 리스트의 첫 번째 노드로 설정
            }
            idx = 1;
            st = 1;
        }

        // idx로 지정한 위치로 이동하기 위한 반복문
        Node* cur = head;
        for (int i = 1; i < idx; i++) {
            cur = cur->next;
        }

        // nums 순회
        for (int i = st; i < nums.size(); i++) {
            // 새로운 노드 생성
            Node* newNode = getNewNode(nums[i]);
            newNode->next = cur->next;
            cur->next = newNode;
            cur = newNode;
        }

        if (cur->next == nullptr) {     // 현재 위치가 리스트의 끝이라면
            // tail 갱신
            tail = cur;
        }
    }

    void remove(int idx, int cnt) {
        Node* cur = head;
        if (idx == 0) { // 맨 앞에서부터 제거하는 경우
            for (int i = 0; i < cnt; i++) {
                cur = cur->next;
            }
            head = cur; // head 갱신
            return;
        }

        // idx가 0이 아닌 경우 주어진 idx로 이동
        for (int i = 1; i < idx; i++) {
            cur = cur->next;
        }
        Node* anchor = cur; // 현재 위치를 저장하는 보조 포인터

        // cnt만큼의 노드를 건너뛰어 이동
        for (int i = 0; i < cnt; i++) {
            cur = cur->next;
        }
        // anchor가 cnt만큼을 건너뛴 후의 cur의 next를 가리키게 하여 그 사이 범위의 노드를 제거
        anchor->next = cur->next;

        if (anchor->next == nullptr) {
            tail = anchor;
        }
    }

    void add(int data) {
        Node* cur = tail;
        Node* newNode = getNewNode(data);
        cur->next = newNode;
        tail = newNode;
    }

    void print() {
        int cnt = 10;
        Node* cur = head;
        while (cnt-- > 0) {
            cout << cur->data << " ";
            cur = cur->next;
        }
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int T = 10;

    for (int t = 1; t <= T; t++) {
        LinkedList list;
        cout << "#" << t << " ";

        int N;
        cin >> N;

        vector<int> initArr(N);
        for (int i = 0; i < N; i++) {
            cin >> initArr[i];
        }
        list.insert(0, initArr);

        int M;
        cin >> M;

        for (int i = 0; i < M; i++) {
            char cmd;
            cin >> cmd;

            int x, y;
            vector<int> temp;
            switch (cmd) {
            case 'I':
                cin >> x >> y;
                temp = vector<int>(y);
                for (int j = 0; j < y; j++) {
                    cin >> temp[j];
                }
                list.insert(x, temp);
                break;
            case 'D':
                cin >> x >> y;
                list.remove(x, y);
                break;
            case 'A':
                cin >> y;
                for (int j = 0; j < y; j++) {
                    int data;
                    cin >> data;
                    list.add(data);
                }
                break;
            }
        }

        list.print();
        cout << "\n";
    }

    return 0;
}
