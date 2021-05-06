// https://www.acmicpc.net/problem/2178
// 미로 탐색

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

/*
4 6
110110
110110
111111
111101
*/

// 제출시 Main으로 클래스명 변경 및 print 함수 제거
public class MazeNavigation {
	static int n;
	static int m;
	static char[][] maze;
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		n = scanner.nextInt();
		m = scanner.nextInt();
		
		maze = new char[n][m];
		
		// 배열에 초기값 넣기
		for(int i = 0; i < n; i++) {
			String line = scanner.next();
			for(int j = 0; j < m; j++) {
				maze[i][j] = line.charAt(j);
			}
		}
		
		scanner.close();
		
		// 확인용 출력
		print();
		
		// Go !
		int answer = go(0,0);
		
		System.out.println(answer);
	}
	
	static int go(int x, int y) {
		int k = 1;
		maze[x][y] = '2';
		// 확인용 출력
		print();
		
		ArrayList<Integer[]> nextPositions = new ArrayList<Integer[]>();
		nextPositions.add(new Integer[] {x,y});
		
		// 확인용 출력
		nextPositions.forEach((s) -> System.out.println("first) nextPo : "+s[0] + "," + s[1]));
		
		while(maze[n-1][m-1] != '2') {
			ArrayList<Integer[]> tempPositions = new ArrayList<Integer[]>();
			for(int j = 0; j < nextPositions.size(); j++) {
				ArrayList<Integer[]> thisPositions = check(nextPositions.get(j)[0], nextPositions.get(j)[1]);
				
				// 그리기
				for(int i = 0; i < thisPositions.size(); i++) {
					int nextX = thisPositions.get(i)[0];
					int nextY = thisPositions.get(i)[1];
					maze[nextX][nextY] = '2';
					tempPositions.add(new Integer[] {nextX, nextY});
					
				}
				
			}
			nextPositions = tempPositions;
			// 확인용 출력
			nextPositions.forEach((s) -> System.out.println("nextPo : "+s[0] + "," + s[1]));
			print();
			k++;
		}
		
		return k;
		
	}
	
	// 현재 좌표를 인수로 받고 갈 수 있는 좌표들을 list로 반환
		static ArrayList<Integer[]> check(int x, int y) {
			ArrayList<Integer[]> list = new ArrayList<Integer[]>();
			
			if(x != 0) {
				if(maze[x -1][y] == '1') {
					list.add(new Integer[] {x-1,y});
				}
			}
			if(y != 0) {
				if(maze[x][y-1] == '1') {
					list.add(new Integer[] {x,y-1});
				}
			}
			if(x + 1 != n) {
				if(maze[x+1][y] == '1') {
					list.add(new Integer[] {x+1,y});
				}
			}
			if(y + 1 != m) {
				if(maze[x][y+1] == '1') {
					list.add(new Integer[] {x,y+1});
				}
			}
			
			return list;
		}
	// 확인용 출력 함수
	static void print() {
		for(char[] line : maze) {
			System.out.println(Arrays.toString(line));
		}
		System.out.println("\n=========================\n");
	}
}