#include <stdio.h>
#include <string.h>



int main(int argc, char** argv) {
    char buf[200];
    char secret_password[256] = "S3cr3tP@ssw0rd";
    char msg[256] = "This is a very innocent message.";
    int start;
    int end;
    printf("Skriv inn starten på meldingen også slutten\n");
    scanf("%d\n", &start);
    scanf("%d\n", &end);
    snprintf(buf,(end-start) + 1,"%s",&msg[start]);
    printf("Contents: %s\n",buf);
    return 0;
}
