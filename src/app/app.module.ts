import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MessagesModule } from 'primeng/messages';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

// My Imports
//import { PsalmModule } from './psalm/psalm.module';
import { CoreModule } from './core/core.module';
import { PsalmModule } from './psalm/psalm.module';

@NgModule( {
    declarations: [
        AppComponent,
    ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        BrowserAnimationsModule,

        // PrimeNG
        MessagesModule,

        // My Imports
        //        PsalmModule,
        CoreModule,
        PsalmModule,
    ],
    providers: [],
    bootstrap: [AppComponent]
} )
export class AppModule { }
