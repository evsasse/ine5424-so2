#include <iostream>

template<int a, int b>
struct MultBySum
{ enum { RET = MultBySum<a-1, b>::RET + b };
};

template <int b>
struct MultBySum<0, b>
{ enum  { RET = 0 };
};

int main(){
  std::cout << MultBySum<2,2>::RET << std::endl;
  std::cout << MultBySum<3,3>::RET << std::endl;
  std::cout << MultBySum<4,4>::RET << std::endl;
}
