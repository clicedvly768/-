#include "wm.h"
#include <stdio.h>
#include <X11/keysym.h>

typedef struct {
    Window window;
    struct Node* next;
} Node;

Node* windows = NULL;

void handle_map_request(XMapRequestEvent e) {
    unsigned long black = BlackPixel(wm.display, wm.screen);
    unsigned long white = WhitePixel(wm.display, wm.screen);
    
    XWindowAttributes attr;
    XGetWindowAttributes(wm.display, e.window, &attr);
    
    Window frame = XCreateSimpleWindow(wm.display, wm.root,
                                       100, 100, attr.width + 10, attr.height + 30,
                                       2, black, white);
    
    XReparentWindow(wm.display, e.window, frame, 5, 25);
    XMapWindow(wm.display, frame);
    XMapWindow(wm.display, e.window);
    
    XSetInputFocus(wm.display, e.window, RevertToParent, CurrentTime);
}

void handle_key_press(XKeyEvent e) {
    if (e.state & Mod1Mask) {
        KeySym key = XLookupKeysym(&e, 0);
        if (key == XK_F4) exit(0);
        if (key == XK_Return) {
            system("xterm &");
        }
    }
}

void handle_button_press(XButtonEvent e) {
    if (e.button == Button1) {
        Window root, child;
        int root_x, root_y, win_x, win_y;
        unsigned int mask;
        if (XQueryPointer(wm.display, e.window,
                         &root, &child,
                         &root_x, &root_y,
                         &win_x, &win_y,
                         &mask)) {
            XSetInputFocus(wm.display, e.window, RevertToParent, CurrentTime);
        }
    }
}
