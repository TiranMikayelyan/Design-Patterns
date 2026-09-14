#include <iostream>
#include <string>

class Logger {
public:
    static Logger& getInstance() {
        static Logger instance;
        return instance;
    }

    void log(const std::string& message) {
        std::cout << message << std::endl;
    }
    Logger(const Logger&) = delete; //argelum enq copy-n
    Logger& operator=(const Logger&) = delete;

private:
    Logger() = default; //private constr
    ~Logger() = default; //private destr
};

int main() {
    Logger& logger1 = Logger::getInstance();
    Logger& logger2 = Logger::getInstance();

    logger1.log("First message");
    logger2.log("Second message");

    std::cout << (&logger1 == &logger2) << std::endl;

    return 0;
}
