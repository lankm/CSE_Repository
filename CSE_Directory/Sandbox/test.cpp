#include <iostream>
#include <algorithm>
#include <chrono>
#include <cstring>
#include <iterator>

#include <stdint.h>

class Position {
    public:
        int64_t pos[3];
        int32_t vel[3];
        uint32_t time;

        Position(int64_t pos[3]) {
            std::memcpy(this->pos, pos, sizeof(this->pos));
            this->time = 0;
            std::memset(this->vel, 0, sizeof(this->pos));
        }

        friend std::ostream& operator<<(std::ostream& os, const Position& obj) {
            std::copy(std::begin(obj.pos), std::end(obj.pos), std::ostream_iterator<int64_t>(os, " "));
            os << std::endl;

            os << obj.time;
            os << std::endl;

            std::copy(std::begin(obj.vel), std::end(obj.vel), std::ostream_iterator<int64_t>(os, " "));

            return os;
        }
        
};

int main(int argc, char **argv) {
    int64_t pos[3] = {1,2,3};

    Position p = Position(pos);

    std::cout << p << std::endl;

    return 0;
}