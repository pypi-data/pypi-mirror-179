// import LabelStudio from 'label-studio';
// import 'label-studio/build/static/css/main.css';
//
// import React, { useEffect } from 'react';
//
// const LabelingInterface = (props: any) => {
//   useEffect(() => {
//     const { projectInfo } = props;
//
//     new LabelStudio('labelstudio', {
//       config: projectInfo.view,
//
//       interfaces: [
//         'panel',
//         'update',
//         'submit',
//         'skip',
//         'controls',
//         'infobar',
//         'topbar',
//         'instruction',
//         'side-column',
//         'ground-truth',
//         'annotations:history',
//         'annotations:tabs',
//         'annotations:menu',
//         'annotations:current',
//         'annotations:add-new',
//         'annotations:delete',
//         'annotations:view-all',
//         'predictions:tabs',
//         'predictions:menu',
//         'auto-annotation',
//         'edit-history',
//         'topbar:prevnext'
//       ],
//
//       user: {
//         pk: 1,
//         firstName: 'James',
//         lastName: 'Dean'
//       },
//       task: {
//         annotations: [],
//         predictions: [],
//         id: 1,
//         data: {
//           image:
//             'https://htx-misc.s3.amazonaws.com/opensource/label-studio/examples/images/nick-owuor-astro-nic-visuals-wDifg5xc9Z4-unsplash.jpg'
//         }
//       },
//       //TODO: any type modification
//       onLabelStudioLoad: function (LS: any) {
//         const c = LS.annotationStore.addAnnotation({
//           userGenerate: true
//         });
//         LS.annotationStore.selectAnnotation(c.id);
//       },
//
//       onSubmitAnnotation: function (LS: any, annotation: any) {
//         // retrive an annotation
//         console.log(annotation.serializeAnnotation());
//       }
//     });
//   });
//
//   return(
//     <div id='labelstudio'/>
//   )
// }
