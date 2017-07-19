#include <iostream>       // std::cout, std::endl
#include <thread>         // std::this_thread::sleep_for
#include <chrono>         // std::chrono::seconds

#include <zipkin.hpp>

int main(int argc, char **argv)
{
  // google::InitGoogleLogging(argv[0]);
std::unique_ptr<zipkin::HttpConf> conf(new zipkin::HttpConf("http://localhost:9411/api/v1/spans"));
std::shared_ptr<zipkin::HttpCollector> collector(conf->create());
std::unique_ptr<zipkin::Tracer> tracer(zipkin::Tracer::create(collector.get()));

if (collector.get()) conf.release();

zipkin::Span& span = *tracer->span("encode");
zipkin::Span::Scope scope(span);

  std::cout << "countdown:\n";
  for (int i=5; i>0; --i) {
    std::cout << i << std::endl;
    std::this_thread::sleep_for (std::chrono::seconds(1));
  }
  std::cout << "Lift off!\n";
  return 0;
}
