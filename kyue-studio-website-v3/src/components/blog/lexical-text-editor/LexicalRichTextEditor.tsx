// /**
//  * Copyright (c) Meta Platforms, Inc. and affiliates.
//  *
//  * This source code is licensed under the MIT license found in the
//  * LICENSE file in the root directory of this source tree.
//  *
//  */

// import {AutoFocusPlugin} from '@lexical/react/LexicalAutoFocusPlugin';
// import {LexicalComposer} from '@lexical/react/LexicalComposer';
// import {ContentEditable} from '@lexical/react/LexicalContentEditable';
// import {LexicalErrorBoundary} from '@lexical/react/LexicalErrorBoundary';
// import {HistoryPlugin} from '@lexical/react/LexicalHistoryPlugin';
// import {RichTextPlugin} from '@lexical/react/LexicalRichTextPlugin';
// import {
//   $isTextNode,
//   DOMConversionMap,
//   DOMExportOutput,
//   DOMExportOutputMap,
//   isHTMLElement,
//   Klass,
//   LexicalEditor,
//   LexicalNode,
//   ParagraphNode,
//   TextNode,
// } from 'lexical';

// import ExampleTheme from './ExampleTheme';
// import ToolbarPlugin from './ToolbarPlugin';
// import TreeViewPlugin from './TreeViewPlugin';
// import {parseAllowedColor, parseAllowedFontSize} from './styleConfig';
// import './styleConfig'

// // plugin for saving data?
// // import OnChangePlugin from '@lexical/react/LexicalOnChangePlugin';
// import {OnChangePlugin} from '@lexical/react/LexicalOnChangePlugin';
// import {EditorState} from 'lexical';
// import { $convertToMarkdownString } from '@lexical/markdown';
// import { useLexicalComposerContext } from '@lexical/react/LexicalComposerContext';
// import {forwardRef, useImperativeHandle} from 'react';
// // import {$generateMarkdownFromNodes} from '@lexical/markdown';
// import $generateMarkdownFromNodes from '@lexical/markdown';
// import { TRANSFORMERS } from '@lexical/markdown';

// // TODO AFTER AWS:Extra plugins from lexical
// // https://lexical.dev/docs/react/plugins#lexicalonchangeplugin


// const placeholder = 'Enter some rich text...';

// const removeStylesExportDOM = (
//   editor: LexicalEditor,
//   target: LexicalNode,
// ): DOMExportOutput => {
//   const output = target.exportDOM(editor);
//   if (output && isHTMLElement(output.element)) {
//     // Remove all inline styles and classes if the element is an HTMLElement
//     // Children are checked as well since TextNode can be nested
//     // in i, b, and strong tags.
//     for (const el of [
//       output.element,
//       ...output.element.querySelectorAll('[style],[class],[dir="ltr"]'),
//     ]) {
//       el.removeAttribute('class');
//       el.removeAttribute('style');
//       if (el.getAttribute('dir') === 'ltr') {
//         el.removeAttribute('dir');
//       }
//     }
//   }
//   return output;
// };

// const exportMap: DOMExportOutputMap = new Map<
//   Klass<LexicalNode>,
//   (editor: LexicalEditor, target: LexicalNode) => DOMExportOutput
// >([
//   [ParagraphNode, removeStylesExportDOM],
//   [TextNode, removeStylesExportDOM],
// ]);

// const getExtraStyles = (element: HTMLElement): string => {
//   // Parse styles from pasted input, but only if they match exactly the
//   // sort of styles that would be produced by exportDOM
//   let extraStyles = '';
//   const fontSize = parseAllowedFontSize(element.style.fontSize);
//   const backgroundColor = parseAllowedColor(element.style.backgroundColor);
//   const color = parseAllowedColor(element.style.color);
//   if (fontSize !== '' && fontSize !== '15px') {
//     extraStyles += `font-size: ${fontSize};`;
//   }
//   if (backgroundColor !== '' && backgroundColor !== 'rgb(255, 255, 255)') {
//     extraStyles += `background-color: ${backgroundColor};`;
//   }
//   if (color !== '' && color !== 'rgb(0, 0, 0)') {
//     extraStyles += `color: ${color};`;
//   }
//   return extraStyles;
// };

// const constructImportMap = (): DOMConversionMap => {
//   const importMap: DOMConversionMap = {};

//   // Wrap all TextNode importers with a function that also imports
//   // the custom styles implemented by the playground
//   for (const [tag, fn] of Object.entries(TextNode.importDOM() || {})) {
//     importMap[tag] = (importNode) => {
//       const importer = fn(importNode);
//       if (!importer) {
//         return null;
//       }
//       return {
//         ...importer,
//         conversion: (element) => {
//           const output = importer.conversion(element);
//           if (
//             output === null ||
//             output.forChild === undefined ||
//             output.after !== undefined ||
//             output.node !== null
//           ) {
//             return output;
//           }
//           const extraStyles = getExtraStyles(element);
//           if (extraStyles) {
//             const {forChild} = output;
//             return {
//               ...output,
//               forChild: (child, parent) => {
//                 const textNode = forChild(child, parent);
//                 if ($isTextNode(textNode)) {
//                   textNode.setStyle(textNode.getStyle() + extraStyles);
//                 }
//                 return textNode;
//               },
//             };
//           }
//           return output;
//         },
//       };
//     };
//   }

//   return importMap;
// };

// const editorConfig = {
//   html: {
//     export: exportMap,
//     import: constructImportMap(),
//   },
//   namespace: 'React.js Demo',
//   nodes: [ParagraphNode, TextNode],
//   onError(error: Error) {
//     throw error;
//   },
//   theme: ExampleTheme,
// };

// // TODO: SAVE TO VARIABLE WHEN SUBMITS-----------------------------------------------------------
// // const [editor] = useLexicalComposerContext();

// // function OnChange( editorState: EditorState ) {
// //   editorState.read(() => {
// //     const json = editorState.toJSON(); // ??? what does this do ??? prob delete tbh
// //     // console.log("Saving json to db ??? {json}", json);

// //     // save probably
// //     const markdown = $convertToMarkdownString(editor, TRANSFORMERS);
// //     console.log({markdown});
// //   })
// // }

// // Send the data to the parent component??
// export interface LexicalEditorHandle {
//   getMarkdown: () => string;
// }


// // React UI Rendering ---------------------------------------------------------------------------------
// const LexicalRichTextEditor = forwardRef<LexicalEditorHandle>((_, ref) => {
//     const [editor] = useLexicalComposerContext();

//   useImperativeHandle(ref, () => ({
//     getMarkdown: () => {
//       let markdown = '';
//       editor.getEditorState().read(() => {
//         markdown = $convertToMarkdownString(TRANSFORMERS);
//         // markdown = $generateMarkdownFromNodes(editor, TRANSFORMERS);
//       });
//       // const markdown = editorState.read(() => {
//       //   return $generateMarkdownFromNodes(editor, TRANSFORMERS);
//       // });
//       return markdown;
//     }
//   }));
  
//   return (
//     <LexicalComposer initialConfig={editorConfig}>
//       <div className="editor-container">
//         <ToolbarPlugin />
//         <div className="editor-inner">
//           <RichTextPlugin
//             contentEditable={
//               <ContentEditable
//                 className="editor-input"
//                 aria-placeholder={placeholder}
//                 placeholder={
//                   <div className="editor-placeholder">{placeholder}</div>
//                 }
//               />
//             }
//             ErrorBoundary={LexicalErrorBoundary}
//           />
//           <HistoryPlugin />
//           <AutoFocusPlugin />
//           <TreeViewPlugin />
          
//           {/* TODO: WIP in progress , to save data to backend // MAYBE DO THIS ALL IN THE PARENT COMPONENT ???? */} 
//           {/* <OnChangePlugin onChange={OnChange} />  */}
//           {/* <OnChange/> */}
//           {/* maybe you can save this since save drafts or wip...? eh idk would cost a lot on dynamodb calls maybe eh idk */}
//         </div>
//       </div>
//     </LexicalComposer>
//   );
// });

// export default LexicalRichTextEditor;
import {
  useLexicalComposerContext,
} from '@lexical/react/LexicalComposerContext';
import { $convertToMarkdownString, TRANSFORMERS } from '@lexical/markdown';
import {
  RichTextPlugin,
} from '@lexical/react/LexicalRichTextPlugin';
import { ContentEditable } from '@lexical/react/LexicalContentEditable';
import { HistoryPlugin } from '@lexical/react/LexicalHistoryPlugin';
import { AutoFocusPlugin } from '@lexical/react/LexicalAutoFocusPlugin';
import { LexicalErrorBoundary } from '@lexical/react/LexicalErrorBoundary';

import ToolbarPlugin from './ToolbarPlugin';
import TreeViewPlugin from './TreeViewPlugin';
import ExampleTheme from './ExampleTheme';

import { forwardRef, useImperativeHandle } from 'react';
// import LexicalComposer from '@lexical/react/LexicalComposer';
import { LexicalComposer } from '@lexical/react/LexicalComposer';
import React, { useState, useEffect } from 'react';

export interface LexicalEditorHandle {
  getMarkdown: () => string;
}

const placeholder = 'Enter some rich text...';

const editorConfig = {
  namespace: 'React.js Demo',
  theme: ExampleTheme,
  onError(error: Error) {
    throw error;
  },
  nodes: [],
};

const LexicalEditorContent = forwardRef<LexicalEditorHandle>((_, ref) => {
  const [editor] = useLexicalComposerContext();

  useImperativeHandle(ref, () => ({
    getMarkdown: () => {
      let markdown = '';
      editor.getEditorState().read(() => {
        markdown = $convertToMarkdownString(TRANSFORMERS);
      });
      return markdown;
    },
  }));

  return (
    <>
      <ToolbarPlugin />
      <div className="editor-inner">
        <RichTextPlugin
          contentEditable={
            <ContentEditable className="editor-input" />
          }
          placeholder={<div className="editor-placeholder">{placeholder}</div>}
          ErrorBoundary={LexicalErrorBoundary}
        />
        <HistoryPlugin />
        <AutoFocusPlugin />
        <TreeViewPlugin />
      </div>
    </>
  );
});

const LexicalRichTextEditor = forwardRef<LexicalEditorHandle>((_, ref) => {
  return (
    <LexicalComposer initialConfig={editorConfig}>
      <div className="editor-container">
        <LexicalEditorContent ref={ref} />
      </div>
    </LexicalComposer>
  );
});

export default LexicalRichTextEditor;
