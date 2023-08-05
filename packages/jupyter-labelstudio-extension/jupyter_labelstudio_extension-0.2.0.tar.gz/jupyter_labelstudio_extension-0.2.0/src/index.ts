import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { MainAreaWidget } from '@jupyterlab/apputils';
import { ILauncher } from '@jupyterlab/launcher';
import { LabelStudioWidget } from './labelling';
// import {ImportWidget} from "./import"
// import { PageConfig } from '@jupyterlab/coreutils';
// import { logoIcon } from "./style/icon"

/**
 * The command IDs used by the react-widget plugin.
 */
// eslint-disable-next-line @typescript-eslint/no-unused-vars
namespace CommandIDs {
  export const create = 'create-labelstudio-widget';
  export const importData = 'import';
}

/**
 * Initialization data for the jupyter_labelstudio_extension extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'LabelStudio:plugin',
  autoStart: true,
  optional: [ILauncher],
  activate: async (app: JupyterFrontEnd, launcher: ILauncher) => {
    console.log(
      'JupyterLab extension jupyter_labelstudio_extension is activated!'
    );

    const { commands } = app;
    const command = CommandIDs.create;

    commands.addCommand(command, {
      caption: 'Create an LabelStudio widget',
      label: 'LabelStudio Extension',
      // TODO: add ICON
      execute: () => {
        const content = new LabelStudioWidget();
        const widget = new MainAreaWidget<LabelStudioWidget>({ content });
        widget.title.label = 'LabelStudio Extension';
        widget.title.icon = 'logo-icon';
        app.shell.add(widget, 'main');
      }
    });

    if (launcher) {
      launcher.add({ command });
    }
  }
};

export default plugin;
