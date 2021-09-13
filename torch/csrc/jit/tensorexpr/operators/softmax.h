#pragma once

#include <torch/csrc/jit/tensorexpr/kernel.h>

namespace torch {
namespace jit {
namespace tensorexpr {

Tensor computeSoftmax(
    const std::vector<ArgValue>& inputs,
    const std::vector<ExprHandle>& outputShape,
    bool log_softmax,
    const std::string name = std::string());

} // namespace tensorexpr
} // namespace jit
} // namespace torch
