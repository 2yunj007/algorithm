#include<iostream>
#include<vector>

using namespace std;

struct Node {
	vector<int> children;
    int parents;
    
    Node() : parents(0) {}
};
/*
Node() {
    parents = 0;
}
*/
int ans, N, M, A, B;
Node* nodes;
vector<int> ancestorA, ancestorB;	// 조상 노드 벡터

// ancestor에 루트 노드부터 조상들을 저장
void traverse(int idx, vector<int>& ancestor) {
	int parent = nodes[idx].parents;
    if (parent != 0) {
        traverse(parent, ancestor);
    }
    // 루트가 가장 먼저 저장, 자기자신은 마지막에 (전위 순회)
    ancestor.push_back(idx);
}

// 서브트리의 개수
int dfs(int idx) {
	int res = 1;
    // 자식 순회
    for (int child : nodes[idx].children) {
    	res += dfs(child);
    }
    return res;
}

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;
    
	for(test_case = 1; test_case <= T; ++test_case) {
        cin >> N >> M >> A >> B;
        nodes = new Node[N + 1]; // 구조체 배열을 동적으로 할당
        // 테스트 케이스에서 사용할 조상 노드 벡터들을 초기화
        ancestorA.clear();
        ancestorB.clear();
        
        for (int i = 0; i < N + 1; i++) { 
        	nodes[i] = Node();	// 각 노드 초기화
        }
        
        for (int i = 0; i < M; i++) {
        	int p, c;
            cin >> p >> c;
            // 부모, 자식 정보 저장
            nodes[p].children.push_back(c);
            nodes[c].parents = p;
        }
        
        // 조상 노드 벡터 만듦
        traverse(A, ancestorA);
        traverse(B, ancestorB);
        
        // 루트부터 조상 탐색
        for (int i = 0; i < N; i++) {
        	// 트리가 갈라지는 경우
            if (ancestorA[i] != ancestorB[i]) break;
            ans = ancestorA[i];
        }
        
        cout << "#" << test_case << " " << ans << " " << dfs(ans) << endl;
        
        delete[] nodes;	// 동적으로 할당한 배열의 메모리를 해제
	}
	return 0;
}