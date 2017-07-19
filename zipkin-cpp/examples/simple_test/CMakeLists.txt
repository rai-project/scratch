set (simple_test_SRCS
    main.cpp
    )

add_executable(simple_test ${simple_test_SRCS})
target_link_libraries(simple_test zipkin ${zipkin_DEPENDENCIES})
