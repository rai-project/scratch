#include <chrono>   // std::chrono::seconds
#include <iostream> // std::cout, std::endl
#include <thread>   // std::this_thread::sleep_for

#include <zipkin.hpp>

int main(int argc, char **argv) {
  google::InitGoogleLogging(argv[0]);
  const auto url = "http://127.0.0.1:9411/api/v1/spans";
  std::unique_ptr<zipkin::HttpConf> conf(new zipkin::HttpConf(url));
  std::unique_ptr<zipkin::HttpCollector> collector(conf->create());
  std::unique_ptr<zipkin::Tracer> tracer(
      zipkin::Tracer::create(collector.get()));

  if (collector.get()) {
    conf.release();
  }

  sockaddr_in addr;
  addr.sin_addr.s_addr = inet_addr("127.0.0.1");
  addr.sin_port = htons(9411);

  // dropdown_name is the one that shows up in the zipkin dropdown
  const zipkin::Endpoint endpoint("dropdown_name", &addr);

  for (int ii = 0; ii < 2; ii++) {
    // trace_name is the name of the trace
    zipkin::Span &span = *tracer->span("trace_name");
    zipkin::Span::Scope scope(span);

    span.client_send(&endpoint);

    span << std::make_pair("some_tag", "0.3." + std::to_string(ii));
    span << std::make_pair("another_tag", std::to_string(ii));
    span << std::make_pair("something_else", "something_else");
  }
  collector->shutdown(std::chrono::seconds(5));
  return 0;
}