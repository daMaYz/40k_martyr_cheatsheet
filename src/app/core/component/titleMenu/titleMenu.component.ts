import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';
import { MenubarModule } from 'primeng/menubar';

@Component( {
    selector: 'titleMenu',
    templateUrl: './titleMenu.component.html'
} )

export class TitleMenuComponent implements OnInit {
    leftItems: MenuItem[];
    rightItems: MenuItem[];

    ngOnInit() {
        this.leftItems = [
            {
                label: 'Home',
                routerLink: ['/'],
            },
            {
                separator: false,
                style: {
                    'pointer-events': 'none',
                    background: 'inherit',
                },
            },
            {
                label: 'Psalm',
                items: [
                    {
                        label: 'Psalms',
                        routerLink: ['/psalm/overview'],
                    },
                    {
                        label: 'Doctrines',
                        routerLink: ['/psalm/doctrine/overview'],
                    },
                ]
            },
        ];



        this.rightItems = [
            {
//                label: 'Stuff',
//                items: [
//                    {
//                        label: 'h2-console',
//                        url: '/h2-console',
//                    },
//                    {
//                        label: 'Manage Enities',
//                        url: '/manage',
//                    },
//                ]
            },
        ];
    }
}
