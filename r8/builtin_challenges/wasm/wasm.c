#include <stdio.h>
#include <string.h>
#include <emscripten.h>



int main(int argc, char** argv) {
    char buf[200];
    char secret_password[256] = "S3cr3tP@ssw0rd";
    char msg[32] = "This is a very innocent message.";
    int start = EM_ASM_INT({
        let start = window.prompt("Skriv inn hvor du vil starte å lese meldingen fra");
        return start
    });
    int end = EM_ASM_INT({
        let end = window.prompt("Skriv inn hvor du vil slutte å lese meldingen fra");
        return end
    });
    snprintf(buf,(end-start) + 1,"%s",&msg[start]);
    EM_ASM_({
        setMsg($0)
    }, buf);
    return 0;
}
