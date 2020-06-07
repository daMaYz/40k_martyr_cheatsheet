import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MenubarModule } from 'primeng/menubar';

import { TitleMenuComponent } from './component/titleMenu/titleMenu.component';
import { PageNotFoundComponent } from './component/pagenotfound/pagenotfound.component';
import { WelcomePageComponent } from './component/welcomePage/welcomePage.component';


@NgModule( {
    imports: [
        CommonModule,
        MenubarModule,
    ],
    declarations: [
        TitleMenuComponent,
        WelcomePageComponent,
        PageNotFoundComponent
    ],
    exports: [
        TitleMenuComponent,
    ],
    providers: []
} )
export class CoreModule { }
