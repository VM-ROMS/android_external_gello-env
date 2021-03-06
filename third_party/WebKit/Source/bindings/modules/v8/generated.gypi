# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'bindings_modules_v8_output_dir': '<(SHARED_INTERMEDIATE_DIR)/blink/bindings/modules/v8',
    'bindings_modules_v8_generated_union_type_files': [
      '<(bindings_modules_v8_output_dir)/ArrayBufferOrArrayBufferViewOrDictionary.cpp',
      '<(bindings_modules_v8_output_dir)/ArrayBufferOrArrayBufferViewOrDictionary.h',
      '<(bindings_modules_v8_output_dir)/ArrayBufferOrArrayBufferViewOrUSVString.cpp',
      '<(bindings_modules_v8_output_dir)/ArrayBufferOrArrayBufferViewOrUSVString.h',
      '<(bindings_modules_v8_output_dir)/ArrayBufferViewOrBlobOrStringOrFormData.cpp',
      '<(bindings_modules_v8_output_dir)/ArrayBufferViewOrBlobOrStringOrFormData.h',
      '<(bindings_modules_v8_output_dir)/BooleanOrMediaTrackConstraints.cpp',
      '<(bindings_modules_v8_output_dir)/BooleanOrMediaTrackConstraints.h',
      '<(bindings_modules_v8_output_dir)/ClientOrServiceWorkerOrMessagePort.cpp',
      '<(bindings_modules_v8_output_dir)/ClientOrServiceWorkerOrMessagePort.h',
      '<(bindings_modules_v8_output_dir)/DictionaryOrString.cpp',
      '<(bindings_modules_v8_output_dir)/DictionaryOrString.h',
      '<(bindings_modules_v8_output_dir)/FormDataOrURLSearchParams.cpp',
      '<(bindings_modules_v8_output_dir)/FormDataOrURLSearchParams.h',
      '<(bindings_modules_v8_output_dir)/HTMLImageElementOrHTMLVideoElementOrHTMLCanvasElementOrImageBitmap.cpp',
      '<(bindings_modules_v8_output_dir)/HTMLImageElementOrHTMLVideoElementOrHTMLCanvasElementOrImageBitmap.h',
      '<(bindings_modules_v8_output_dir)/OffscreenCanvasRenderingContext2DOrWebGLRenderingContextOrWebGL2RenderingContext.cpp',
      '<(bindings_modules_v8_output_dir)/OffscreenCanvasRenderingContext2DOrWebGLRenderingContextOrWebGL2RenderingContext.h',
      '<(bindings_modules_v8_output_dir)/RTCIceCandidateInitOrRTCIceCandidate.cpp',
      '<(bindings_modules_v8_output_dir)/RTCIceCandidateInitOrRTCIceCandidate.h',
      '<(bindings_modules_v8_output_dir)/RenderingContext.cpp',
      '<(bindings_modules_v8_output_dir)/RenderingContext.h',
      '<(bindings_modules_v8_output_dir)/RequestOrUSVString.cpp',
      '<(bindings_modules_v8_output_dir)/RequestOrUSVString.h',
      '<(bindings_modules_v8_output_dir)/ServiceWorkerOrMessagePort.cpp',
      '<(bindings_modules_v8_output_dir)/ServiceWorkerOrMessagePort.h',
      '<(bindings_modules_v8_output_dir)/StringOrArrayBufferOrNFCMessage.cpp',
      '<(bindings_modules_v8_output_dir)/StringOrArrayBufferOrNFCMessage.h',
      '<(bindings_modules_v8_output_dir)/StringOrCanvasGradientOrCanvasPattern.cpp',
      '<(bindings_modules_v8_output_dir)/StringOrCanvasGradientOrCanvasPattern.h',
      '<(bindings_modules_v8_output_dir)/StringOrStringSequence.cpp',
      '<(bindings_modules_v8_output_dir)/StringOrStringSequence.h',
      '<(bindings_modules_v8_output_dir)/StringOrStringSequenceOrDOMStringList.cpp',
      '<(bindings_modules_v8_output_dir)/StringOrStringSequenceOrDOMStringList.h',
      '<(bindings_modules_v8_output_dir)/StringOrUnsignedLong.cpp',
      '<(bindings_modules_v8_output_dir)/StringOrUnsignedLong.h',
      '<(bindings_modules_v8_output_dir)/UnsignedLongOrUnsignedLongSequence.cpp',
      '<(bindings_modules_v8_output_dir)/UnsignedLongOrUnsignedLongSequence.h',
    ],

    'conditions': [
      ['OS=="win" and buildtype=="Official"', {
        # On Windows Official release builds, we try to preserve symbol
        # space.
        'bindings_modules_v8_generated_aggregate_files': [
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings.cpp',
        ],
      }, {
        'bindings_modules_v8_generated_aggregate_files': [
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings01.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings02.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings03.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings04.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings05.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings06.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings07.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings08.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings09.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings10.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings11.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings12.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings13.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings14.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings15.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings16.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings17.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings18.cpp',
          '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindings19.cpp',
        ],
      }],
    ],
    'bindings_modules_v8_generated_partial_aggregate_files': [
      '<(bindings_modules_v8_output_dir)/V8GeneratedModulesBindingsPartial.cpp',
    ],
  },
}
