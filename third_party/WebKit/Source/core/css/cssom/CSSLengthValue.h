// Copyright 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef CSSLengthValue_h
#define CSSLengthValue_h

#include "core/css/cssom/StyleValue.h"

namespace blink {

class CalcDictionary;
class ExceptionState;

class CORE_EXPORT CSSLengthValue : public StyleValue {
    WTF_MAKE_NONCOPYABLE(CSSLengthValue);
    DEFINE_WRAPPERTYPEINFO();
public:
    static CSSPrimitiveValue::UnitType unitFromName(const String& name);

    CSSLengthValue* add(const CSSLengthValue* other, ExceptionState&);
    CSSLengthValue* subtract(const CSSLengthValue* other, ExceptionState&);
    CSSLengthValue* multiply(double, ExceptionState&);
    CSSLengthValue* divide(double, ExceptionState&);

    virtual bool containsPercent() const = 0;

    static CSSLengthValue* from(const String& cssString, ExceptionState&);
    static CSSLengthValue* from(double value, const String& typeStr, ExceptionState&);
    static CSSLengthValue* from(const CalcDictionary&, ExceptionState&);

protected:
    CSSLengthValue() {}

    virtual CSSLengthValue* addInternal(const CSSLengthValue* other, ExceptionState&);
    virtual CSSLengthValue* subtractInternal(const CSSLengthValue* other, ExceptionState&);
    virtual CSSLengthValue* multiplyInternal(double, ExceptionState&);
    virtual CSSLengthValue* divideInternal(double, ExceptionState&);

    static bool isSupportedLengthUnit(CSSPrimitiveValue::UnitType unit)
    {
        return (CSSPrimitiveValue::isLength(unit) || unit == CSSPrimitiveValue::UnitType::Percentage)
            && unit != CSSPrimitiveValue::UnitType::QuirkyEms
            && unit != CSSPrimitiveValue::UnitType::UserUnits;
    }

    static const int kNumSupportedUnits = 15;
};

DEFINE_TYPE_CASTS(CSSLengthValue, StyleValue, value,
    (value->type() == StyleValue::SimpleLengthType
        || value->type() == StyleValue::CalcLengthType),
    (value.type() == StyleValue::SimpleLengthType
        || value.type() == StyleValue::CalcLengthType));

} // namespace blink

#endif
